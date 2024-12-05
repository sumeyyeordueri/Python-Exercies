# 3. Pounds to Kilograms
# One pound is equivalent to 0.454 kilograms. Write a program that asks the user to enter the mass of an object in pounds and then calculates and displays the mass of the object in kilograms. 

# Ask the user to enter the mass of an object in pounds
mass_pounds = float(input("Enter the mass of the object in pounds: "))

# Convert the mass to kilograms (1 pound = 0.454 kilograms)
mass_kilograms = mass_pounds * 0.454

# Display the mass in kilograms
print(f"The mass of the object in kilograms is: {mass_kilograms:.3f} kg")
