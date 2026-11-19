prices = {
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive": 400,
    "Camera": 5000
}

# Ask the user for discount percentage
discount = float(input("Enter discount percentage: "))

total = 0
discounted_total = 0

# Open file in write mode
with open("discount_report.txt", "w") as file:

    file.write("Product | Original Price | Discounted Price\n")
    file.write("--------------------------------------------\n")

    for product, price in prices.items():
        discounted_price = price - (price * discount / 100)

        file.write(product + " | " + str(price) + " | " + str(discounted_price) + "\n")

        total += 1
        discounted_total += discounted_price

    average = discounted_total / total

    file.write("--------------------------------------------\n")
    file.write("Total Items: " + str(total) + "\n")
    file.write("Average Discounted Price: " + str(average) + "\n")


# Read the file and print its contents
with open("discount_report.txt", "r") as file:
    print("\n----- DISCOUNT REPORT -----")
    print(file.read())
