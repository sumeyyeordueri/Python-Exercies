''' Body Mass Index
Write a program that calculates and displays a person’s body mass index (BMI). The BMI is often used to determine whether a person is overweight or underweight for his or her height. A person’s BMI is calculated with the following formula:
BMI 5 weight 3 703/height2
where weight is measured in pounds and height is measured in inches. The program should ask the user to enter his or her weight and height, then display the user’s BMI. The pro- gram should also display a message indicating whether the person has optimal weight, is underweight, or is overweight. A person’s weight is considered to be optimal if his or her BMI is between 18.5 and 25. If the BMI is less than 18.5, the person is considered to be underweight. If the BMI value is greater than 25, the person is considered to be overweight.''' 

# BMI Calculator

def calculate_bmi(weight, height):
    """
    Calculate BMI using the formula BMI = (weight * 703) / (height^2).
    """
    return (weight * 703) / (height ** 2)

def get_bmi_category(bmi):
    """
    Determine the BMI category.
    """
    if bmi < 18.5:
        return "underweight"
    elif 18.5 <= bmi <= 25:
        return "optimal weight"
    else:
        return "overweight"

def main():
    """
    Main function to interact with the user and calculate BMI.
    """
    try:
        # Get user inputs
        weight = float(input("Enter your weight in pounds: "))
        height = float(input("Enter your height in inches: "))

        if weight <= 0 or height <= 0:
            print("Weight and height must be positive values.")
            return

        # Calculate BMI
        bmi = calculate_bmi(weight, height)

        # Get BMI category
        category = get_bmi_category(bmi)

        # Display results
        print(f"Your BMI is: {bmi:.2f}")
        print(f"You are considered {category}.")
    except ValueError:
        print("Invalid input. Please enter numeric values for weight and height.")

if __name__ == "__main__":
    main()
