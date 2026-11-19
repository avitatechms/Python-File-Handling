 Python file handling tasks. It demonstrates how to create, read, write, append, and manage files using Python.

The project uses basic Python concepts without any external libraries.

Task 1: Write Sales Records to a File
Create a list of sales amounts.
Write each sale into sales_data.txt on a new line.
Read the file and print its contents.
Use write (w) mode.

Task 2: Read File in Different Ways
Read the entire file using read().
Read the first line using readline().
Read all lines using readlines().
Convert sales values into integers.

Task 3: Append New Sales
Add new sales amounts to sales_data.txt.
Use append (a) mode.
Read and print the updated file.
Count the total number of sales records.

Task 4: Generate Summary Report
Read all sales values from the file.
Convert values into integers.
Calculate:
Total Sales
Highest Sale
Lowest Sale
Average Sale

Task 5: Create Product Info File
Get 3 product names and prices from the user.
Store product details in products.txt.
Use the format: ProductName | Price.
Read and print the file contents.

Task 6: Read File Safely
Ask the user for a filename.
Check whether the file exists using os.path.exists().
If the file exists, read and print its contents.
If the file does not exist, display an error message.

Task 7: Export Discounted Prices
Create a dictionary containing product names and prices.
Ask the user for a discount percentage.
Calculate discounted prices.
Write the results into discount_report.txt.
Display the report.
Calculate total items and average discounted price.

File Modes Used
-----------------
r	Read a file
w	Write to a file
a	Append data to a file
r+	Read and write a file
w+	Write and read a file


Files Created
--------------
sales_data.txt	Stores sales records
products.txt	Stores product names and prices
discount_report.txt	Stores discounted prices and summary

Requirements
--------------
Python 3.8 or above
Basic knowledge of Python
Any Python code editor (VS Code, PyCharm, IDLE, etc.)

How to Run
-------------
Download or clone this project.
Open the project folder in your code editor.
Run the Python files one by one.
Follow the instructions displayed in the terminal.
Check the generated text files for the results.

Conclusion
-----------
This project helped me understand basic Python file handling operations, including reading, writing, appending, and checking files. It also helped me practice lists, dictionaries, loops, conditions, and basic calculations in Python.