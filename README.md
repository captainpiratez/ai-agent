# AI Code Assistant

An AI-powered coding assistant that uses Google's Gemini API to help you analyze, debug, and modify Python codebases. The agent can read files, run Python scripts, and write code to help you solve programming problems.

## Features

- **File Operations**: List directory contents and read file contents
- **Code Execution**: Run Python files with arguments and capture output
- **Code Writing**: Create and modify Python files
- **Interactive Assistance**: Ask questions about your code and get step-by-step help
- **Calculator Project**: Includes a sample calculator project for testing

## Prerequisites

- Python 3.12 or higher
- Google Gemini API key

## Setup

### 1. Install Dependencies

```bash
# Using uv (recommended)
uv sync

# Or using pip
pip install google-genai python-dotenv
```

### 2. Get a Gemini API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy the API key

### 3. Set Environment Variables

Copy the example environment file and add your API key:

```bash
cp .env.example .env
# Edit .env and replace 'your_api_key_here' with your actual API key
```

Or create a `.env` file manually:

```bash
GEMINI_API_KEY=your_api_key_here
```

Or set the environment variable directly:

```bash
export GEMINI_API_KEY=your_api_key_here
```

## Usage

### Basic Usage

Run the AI assistant with a prompt describing what you want to do:

```bash
python main.py "your prompt here"
```

### Examples

```bash
# Ask for help with the calculator
python main.py "How do I fix the calculator?"

# Ask about code structure
python main.py "What files are in this project and what do they do?"

# Get help with debugging
python main.py "The calculator tests are failing, can you help me debug them?"

# Request code improvements
python main.py "Can you add error handling to the calculator?"

# Ask for new features
python main.py "Add a square root function to the calculator"
```

### Verbose Mode

Use the `--verbose` flag to see detailed information about API calls and function executions:

```bash
python main.py "analyze the calculator code" --verbose
```

## How It Works

The AI assistant operates in an iterative loop:

1. **Receives your prompt** - You describe what you want to accomplish
2. **Plans the approach** - The AI creates a step-by-step plan
3. **Executes functions** - Uses available tools to:
   - List files and directories
   - Read file contents
   - Run Python scripts
   - Write or modify files
4. **Provides results** - Shows you the output and any code changes

## Available Functions

The AI assistant can perform these operations:

- `get_files_info`: List contents of directories
- `get_file_content`: Read the contents of files
- `run_python_file`: Execute Python scripts with optional arguments
- `write_file`: Create or modify files

## Working Directory

By default, the assistant works within the `./calculator` directory. This is configured in `config.py` and can be modified if needed.

## Calculator Project

The repository includes a sample calculator project in the `calculator/` directory:

- `main.py` - Calculator CLI interface
- `pkg/calculator.py` - Calculator logic
- `pkg/render.py` - Output formatting
- `tests.py` - Unit tests

You can test the calculator directly:

```bash
cd calculator
python main.py "3 + 5"
python tests.py
```

## Configuration

Edit `config.py` to modify settings:

- `MAX_CHARS`: Maximum characters for file content (default: 10000)
- `WORKING_DIR`: Directory the AI works in (default: "./calculator")
- `MAX_ITERS`: Maximum iterations per session (default: 20)

## Safety Notes

⚠️ **Important Security Considerations:**

- The AI agent can read, write, and execute files in the working directory
- Be cautious when giving it access to sensitive codebases
- Always commit your changes before running the agent so you can revert if needed
- Review all code changes before applying them to production

## Troubleshooting

### ModuleNotFoundError: No module named 'google'

Install the required dependencies:
```bash
uv sync  # or pip install google-genai python-dotenv
```

### API Key Issues

- Ensure your `GEMINI_API_KEY` is set correctly
- Verify the API key is valid and has appropriate permissions
- Check that the `.env` file is in the project root

### Permission Errors

The agent is restricted to the working directory for security. If you get permission errors, ensure your files are within the configured `WORKING_DIR`.

## Extending the Project

- Fix harder and more complex bugs
- Refactor sections of code
- Add entirely new features
- Other LLM providers
- Other Gemini models
- Giving it more functions to call

## Contributing

Feel free to submit issues and enhancement requests!

