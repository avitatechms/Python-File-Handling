products = []

for i in range(3):
    name = input("Enter product name: ")
    price = input("Enter product price: ")
    products.append((name, price))

# Write product details into products.txt
with open("products.txt", "w") as file:
    for name, price in products:
        file.write(name + " | " + price + "\n")

# Read the file and print each line
with open("products.txt", "r") as file:
    print("\n----- PRODUCT DETAILS -----")

    for line in file:
        print(line.strip())


# products = []
# for i in range(3): products.append((input("Enter product name: "), input("Enter product price: ")))

# products = [((name := input("Enter product name: ")), (price := input("Enter product price: "))) for i in range(3)]

# products = [(input("Enter product name: "), input("Enter product price: ")) for i in range(3)]

