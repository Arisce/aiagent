from functions.run_python_file import run_python_file

print("Test 1: Calculator Usage Instructions")
print(run_python_file("calculator", "main.py"))

print("Test 2: Running the calculator with an expression")
print(run_python_file("calculator", "main.py", ["3 + 5"]))

print("Test 3: Running the calculator test suite")
print(run_python_file("calculator", "tests.py"))

print("Test 4: Attempting to run outside of the directory")
print(run_python_file("calculator", "../main.py"))

print("Test 5: Attempting to use a nonexistent python file")
print(run_python_file("calculator", "nonexistent.py"))

print("Test 6: Attempting to use a non .py file")
print(run_python_file("calculator", "lorem.txt"))