
# Read the entire file using read()
with open("sales_data.txt", "r") as file:
    content = file.read()
    print("Entire File Contents:")
    print(content)


# Read the first line using readline()
with open("sales_data.txt", "r") as file:
    first_line = file.readline()
    print("First Line:")
    print(first_line.strip())


# Read all lines using readlines()
# Convert the lines into a list of integers
with open("sales_data.txt", "r") as file:
    lines = file.readlines()
    sales_list = [int(line.strip()) for line in lines]

    print("All Lines as a List of Integers:")
    print(sales_list)
