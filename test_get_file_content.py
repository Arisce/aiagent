from functions.get_file_content import get_file_content

print("Result for current directory:")
print(get_file_content("calculator", "main.py"))

print("\nResult for 'pkg' directory:")
print(get_file_content("calculator", "pkg/calculator.py"))

print("\nResult for '/bin' directory:")
print(get_file_content("calculator", "/bin/cat"))

print("\nResult for '../' directory:")
print(get_file_content("calculator", "pkg/does_not_exist.py"))