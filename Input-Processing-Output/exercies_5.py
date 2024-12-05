#5. Payment Instalments
#Write a program that asks the user to enter the amount of a purchase and the desired number of payment instalments. The program should add 5 percent to the amount to get the total purchase amount, and then divide it by the desired number of instalments, then display messages telling the user the total amount of the purchase and how much each instalment will cost.

# Ask the user for the purchase amount
purchase_amount = float(input("Enter the purchase amount: "))

# Ask the user for the desired number of instalments
num_instalments = int(input("Enter the number of payment instalments: "))

# Add 5% to the purchase amount to get the total amount
total_amount = purchase_amount * 1.05

# Calculate the cost of each instalment
instalment_cost = total_amount / num_instalments

# Display the results
print(f"The total amount of the purchase (including 5% fee): ${total_amount:.2f}")
print(f"Each instalment will cost: ${instalment_cost:.2f}")
