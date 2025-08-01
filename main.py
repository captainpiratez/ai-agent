import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

from prompts import system_prompt
from call_function import call_function, available_functions
from config import MAX_ITERATION


def main():
    load_dotenv()

    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I fix the calculator?"')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    if verbose:
        print(f"User prompt: {user_prompt}\n")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    run_agent_loop(client, messages, verbose)



def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ),
    )
    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
        print(response.candidates)
    if response.candidates:
        for each in response.candidates:
            messages.append(each.content)

    if not response.function_calls:
        return response.text

    function_responses = []
    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verbose)
        if (
            not function_call_result.parts
            or not function_call_result.parts[0].function_response
        ):
            raise Exception("empty function call result")
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
        function_responses.append(function_call_result.parts[0])

    if not function_responses:
        raise Exception("no function responses generated, exiting.")
    
    # After you've collected all your function_responses
    tool_message = types.Content(role="tool", parts=function_responses)
    messages.append(tool_message)
    
    return (function_responses[0].function_response.response
            if len(function_responses) == 1
            else function_responses)
    # Don't return the function responses - just let the loop continue
    return None


def run_agent_loop(client, messages, verbose):
    for i in range(MAX_ITERATION):
        if verbose:
            print(f"\nIteration {i + 1}/{MAX_ITERATION}")
        try:
            result = generate_content(client, messages, verbose)
        except Exception as e:
            # handle the error
            print(f"Error: {e}")
            break  # or continue, depending on what you want to do
        if result and isinstance(result, str):  # This means we got a final text response

            print("Final response:")
            print(result)
            break  # Exit the loop

if __name__ == "__main__":
    main()
