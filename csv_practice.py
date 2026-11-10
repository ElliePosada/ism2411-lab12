#Reflection
#1. #Doing this task in Python is similar to Excel because both allow you to organize, calculate, and filter data. However, Python makes it easier to automate tasks and work with larger amounts of data without having to repeat the same steps. Excel is more convenient for quickly editing data, creating charts, and viewing information in a spreadsheet.
#2. #A business could use an append-mode log file to keep track of daily sales transactions. Each time a sale is recorded, the information could be added to the log without deleting previous entries. Append mode would be useful because it allows the business to keep a history of transactions and review past sales when needed.

import csv
#Exercise 2: read and print raw rows
with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#Exercise 3: Skip the header
with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)
    
    header = next(reader)
    print("Header:", header)
    for row in reader:
        print(row)


# Exercise 4: Compute totals

total_revenue = 0

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])

        total = price * quantity
        total_revenue += total

        print(f"{product}: {quantity} units x ${price:.2f} = ${total:.2f}")

print(f"Total Revenue: ${total_revenue:.2f}")

# Exercise 5: Filter and write

rows_written = 0
total_rows = 0

with open("data/sales.csv", "r") as infile:
    reader = csv.reader(infile)
    next(reader)

    with open("data/cleaned.csv", "w", newline="") as outfile:
        writer = csv.writer(outfile)

        writer.writerow(["Product", "Price", "Qty", "Total"])

        for row in reader:
            total_rows += 1

            product = row[0]
            price = float(row[1])
            quantity = int(row[2])
            total = price * quantity

            if total > 100:
                writer.writerow([product, price, quantity, round(total, 2)])
                rows_written += 1

print(f"Rows written: {rows_written}")
print(f"Original rows: {total_rows}")

# Exercise 6: CSV DictReader

with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity

        print(f"{product}: {quantity} units x ${price:.2f} = ${total:.2f}")

    print("Finished reading CSV with DictReader.")

# csv.reader is useful when you know the order of the columns.
# csv.DictReader is easier when you want to access data by column name.

# Exercise 7: Summarize sales by product

product_totals = {}

with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity

        if product in product_totals:
            product_totals[product] += total
        else:
            product_totals[product] = total

for product, total in product_totals.items():
    print(f"{product}: ${total:.2f}")

# Exercise 8: Append mode log

from datetime import datetime

total_revenue = 0

with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        price = float(row["price"])
        quantity = int(row["quantity"])
        total_revenue += price * quantity

current_time = datetime.now()

with open("data/run_log.txt", "a") as log_file:
    log_file.write(f"{current_time}: Total Revenue = ${total_revenue:.2f}\n")

print("Revenue logged successfully!")    