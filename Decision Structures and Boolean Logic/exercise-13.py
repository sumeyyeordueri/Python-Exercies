''' Shipping Charges

The Fast Freight Shipping Company charges the following rates:
  Weight of Package
2 pounds or less
Over 2 pounds but not more than 6 pounds Over 6 pounds but not more than 10 pounds Over 10 pounds
Rate per Pound
$1.50 $3.00 $4.00 $4.75
  Write a program that asks the user to enter the weight of a package then displays the ship- ping charges.'''


# Function to calculate the shipping charges based on package weight
def calculate_shipping_charges(weight):
    if weight <= 2:
        rate = 1.50
    elif 2 < weight <= 6:
        rate = 3.00
    elif 6 < weight <= 10:
        rate = 4.00
    else:
        rate = 4.75

    shipping_cost = weight * rate
    return shipping_cost

# Main function
def main():
    print("Welcome to the Fast Freight Shipping Calculator!")

    # Get user input for the weight of the package
    try:
        weight = float(input("Enter the weight of the package in pounds: "))

        if weight <= 0:
            print("Error: The weight of the package must be greater than 0.")
            return

        # Calculate the shipping charges
        shipping_cost = calculate_shipping_charges(weight)

        # Display the shipping charges
        print(f"The shipping cost for a package weighing {weight} pounds is: ${shipping_cost:.2f}")
    
    except ValueError:
        print("Error: Please enter a valid number for the weight of the package.")

# Run the program
main()
