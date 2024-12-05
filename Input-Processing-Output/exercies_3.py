# 3. Total Purchase
# A customer in a store is purchasing five items. Write a program that asks for the price of each item, then displays the subtotal of the sale, the amount of sales tax, and the total. Assume the sales tax is 7 percent.

# Sales tax rate
sales_tax_rate = 0.07

# Ask the user for the price of each item
item1 = float(input("Enter the price of item 1: "))
item2 = float(input("Enter the price of item 2: "))
item3 = float(input("Enter the price of item 3: "))
item4 = float(input("Enter the price of item 4: "))
item5 = float(input("Enter the price of item 5: "))

# Calculate the subtotal
subtotal = item1 + item2 + item3 + item4 + item5

# Calculate the sales tax
sales_tax = subtotal * sales_tax_rate

# Calculate the total
total = subtotal + sales_tax

# Display the results
print(f"Subtotal: ${subtotal:.2f}")
print(f"Sales Tax (7%): ${sales_tax:.2f}")
print(f"Total: ${total:.2f}")
