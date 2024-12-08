''' Number Analyser
Write a program that asks the user to enter an integer. The program should display “Positive” if the number is greater than 0, “Negative” if the number is less than 0, and “Zero” if the number is equal to 0. The program should then display “Even” if the number is even, and “Odd” if the number is odd. '''


# Input: Ask the user to enter an integer
number = int(input("Enter an integer: "))

# Determine if the number is Positive, Negative, or Zero
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# Determine if the number is Even or Odd
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
