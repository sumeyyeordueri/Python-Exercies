#7. Tip, Tax, and Total
#Write a program that calculates the total amount of a meal purchased at a restaurant. The program should ask the user to enter the charge for the food, then calculate the amounts of a 18 percent tip and 7 percent sales tax. Display each of these amounts and the total.

# Ask the user to enter the charge for the food
food_charge = float(input("Enter the charge for the food: "))

# Calculate the tip (18% of the food charge)
tip = food_charge * 0.18

# Calculate the sales tax (7% of the food charge)
sales_tax = food_charge * 0.07

# Calculate the total amount
total_amount = food_charge + tip + sales_tax

# Display the results
print(f"Food Charge: ${food_charge:.2f}")
print(f"Tip (18%): ${tip:.2f}")
print(f"Sales Tax (7%): ${sales_tax:.2f}")
print(f"Total Amount: ${total_amount:.2f}")
