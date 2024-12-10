''' Software Sales
A software company sells a package that retails for $99. Quantity discounts are given according to the following table:
 Quantity   Discount
 10–19        10% 
 20–49        20% 
 50–99        30% 
 100 or more  40%
Write a program that asks the user to enter the number of packages purchased. The pro- gram should then display the amount of the discount (if any) and the total amount of the purchase after the discount. '''

# Function to calculate the discount and total price
def calculate_discount_and_total(quantity):
    price_per_package = 99
    
    if quantity < 10:
        discount = 0
    elif 10 <= quantity <= 19:
        discount = 0.10
    elif 20 <= quantity <= 49:
        discount = 0.20
    elif 50 <= quantity <= 99:
        discount = 0.30
    else:
        discount = 0.40

    total_price = price_per_package * quantity
    discount_amount = total_price * discount
    total_after_discount = total_price - discount_amount
    
    return discount_amount, total_after_discount

# Main function
def main():
    print("Welcome to the Software Sales Program!")
    
    # Get user input for the number of packages purchased
    try:
        quantity = int(input("Enter the number of packages purchased: "))
        
        if quantity < 0:
            print("Error: The number of packages cannot be negative.")
            return
        
        # Calculate the discount and total after discount
        discount_amount, total_after_discount = calculate_discount_and_total(quantity)
        
        # Display the results
        if discount_amount > 0:
            print(f"You received a discount of ${discount_amount:.2f}.")
        print(f"The total cost after the discount is: ${total_after_discount:.2f}.")
        
    except ValueError:
        print("Error: Please enter a valid integer for the number of packages.")

# Run the program
main()
