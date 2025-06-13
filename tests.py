from functions.get_file_content import get_file_content


def test():
    result = get_file_content("calculator", "main.py")
    print("Result for main.txt:")
    print(result)
    print("")

    result = get_file_content("calculator", "pkg/calculator.py")
    print("Result for pkg/calculator.py:")
    print(result)
    print("")

    result = get_file_content("calculator", "/bin/cat")
    print("Result for /bin/cat:")
    print(result)
    print("")
    


if __name__ == "__main__":
    test()
