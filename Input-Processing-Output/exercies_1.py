
# 1. Sales Prediction
# A company has determined that its annual profit is typically 23 percent of total sales. Write a program that asks the user to enter the projected amount of total sales, then displays the profit that will be made from that amount.
# Hint: Use the value 0.23 to represent 23 percent.

# Ask the user to enter the projected total sales
total_sales = float(input("Enter the projected total sales: "))

# Calculate the profit as 23% of total sales
profit = total_sales * 0.23

# Display the profit
print(f"The projected profit is: ${profit:.2f}")
