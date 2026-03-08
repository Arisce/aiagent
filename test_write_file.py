from functions.write_file import write_file

print("Test 1: Write new file")
print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

print("\nTest 2: Write to nested directory")
print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

print("\nTest 3: Attempt to write outside directory")
print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))