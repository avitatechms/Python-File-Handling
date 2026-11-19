new_sales = [5000, 2500, 1700]

# Open the file in append mode
with open("sales_data.txt", "a") as file:
    for sale in new_sales:
        file.write(str(sale) + "\n")

# Reopen the file in read mode and print updated contents
with open("sales_data.txt", "r") as file:
    content = file.read()
    print("Updated Sales Records:")
    print(content)

# Count the total number of lines
with open("sales_data.txt", "r") as file:
    lines = file.readlines()
    print("Total Number of Sales Records:", len(lines))
