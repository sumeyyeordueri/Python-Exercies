'''  Money Counting Game
Create a change-counting game that gets the user to enter the number of coins required to make exactly one dollar. The program should prompt the user to enter the number of pennies, nickels, dimes, and quarters. If the total value of the coins entered is equal to one dollar, the program should congratulate the user for winning the game. Otherwise, the program should display a message indicating whether the amount entered was more than or less than one dollar. '''

# Money Counting Game

# Function to calculate the total value of the coins
def calculate_total(pennies, nickels, dimes, quarters):
    total = (pennies * 0.01) + (nickels * 0.05) + (dimes * 0.10) + (quarters * 0.25)
    return total

# Main function
def main():
    print("Welcome to the Money Counting Game!")
    print("Your goal is to make exactly $1 using coins.")
    
    # User inputs
    try:
        pennies = int(input("Enter the number of pennies (1 cent): "))
        nickels = int(input("Enter the number of nickels (5 cents): "))
        dimes = int(input("Enter the number of dimes (10 cents): "))
        quarters = int(input("Enter the number of quarters (25 cents): "))
        
        # Validate input
        if pennies < 0 or nickels < 0 or dimes < 0 or quarters < 0:
            print("Error: The number of coins cannot be negative.")
            return
        
        # Calculate total
        total = calculate_total(pennies, nickels, dimes, quarters)
        
        # Check the result
        if total == 1.0:
            print("Congratulations! You've made exactly $1. You win the game!")
        elif total > 1.0:
            print(f"Oops! The total value is ${total:.2f}. That's more than $1.")
        else:
            print(f"Oops! The total value is ${total:.2f}. That's less than $1.")
    
    except ValueError:
        print("Error: Please enter valid integers for the number of coins.")

# Run the game
main()
