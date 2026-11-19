
import os

filename = input("Enter the filename to open: ")

# Check whether the file exists
if os.path.exists(filename):
    with open(filename, "r") as file:
        content = file.read()
        print("\nFile Contents:")
        print(content)
else:
    print("File not found. Please check the filename.")
