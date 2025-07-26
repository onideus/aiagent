from functions.run_python import run_python_file


def test():
    result = run_python_file("calculator", "main.py")
    print("Result for running main.py without arguments:")
    print(result)
    print("")

    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print("Result for running calculator with '3 + 5':")
    print(result)
    print("")

    result = run_python_file("calculator", "tests.py")
    print("Result for running tests.py:")
    print(result)
    print("")

    result = run_python_file("calculator", "../main.py")
    print("Result for attempting to run file outside working directory:")
    print(result)
    print("")

    result = run_python_file("calculator", "nonexistent.py")
    print("Result for running non-existent file:")
    print(result)


if __name__ == "__main__":
    test()
