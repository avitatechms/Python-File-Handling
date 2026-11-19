sales = [1200, 450, 980, 1500, 3000]

# Open the file in write mode
with open("sales_data.txt", "w") as file:
    for sale in sales:
        file.write(str(sale) + "\n")

with open("sales_data.txt", "r") as file:
    print("Sales Records:")
    print(file.read())

# with open("sales_data.txt", "w") as file:
#     for i in range(len(sales)):
#         if i > 0:
#             file.write(",")  # comma-separated format instead of separate lines
#         file.write(str(sales[i]))
