#7. Miles-per-Gallon
#A car's miles-per-gallon (MPG) can be calculated with the following formula:
#MPG 5 Miles driven 4 Gallons of gas used
#Write a program that asks the user for the number of miles driven and the gallons of gasused. It should calculate the car's MPG and display the result.

# Ask the user for the number of miles driven
miles_driven = float(input("Enter the number of miles driven: "))

# Ask the user for the gallons of gas used
gallons_used = float(input("Enter the gallons of gas used: "))

# Calculate miles-per-gallon (MPG)
mpg = miles_driven / gallons_used

# Display the result
print(f"The car's miles-per-gallon (MPG) is: {mpg:.2f}")
