
# Open the file in read mode
with open("sales_data.txt", "r") as file:
    lines = file.readlines()

# Convert all sales values into integers
sales = []
for line in lines:
    value = int(line.strip())
    sales.append(value)

# Calculate summary details
total_sales = sum(sales)
highest_sale = max(sales)
lowest_sale = min(sales)
average_sale = total_sales / len(sales)

# Print the summary report
print("----- SALES SUMMARY REPORT -----")
print("Total Sales:", total_sales)
print("Highest Sale:", highest_sale)
print("Lowest Sale:", lowest_sale)
print("Average Sale:", average_sale)


# sales = [int(line.strip()) for line in lines]