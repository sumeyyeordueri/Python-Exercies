''' Mass and Weight
Scientists measure an object’s mass in kilograms and its weight in newtons. If you know the amount of mass of an object in kilograms, you can calculate its weight in newtons with the following formula:
weight 5 mass 3 9.8
Write a program that asks the user to enter an object’s mass, then calculates its weight. If the object weighs more than 500 newtons, display a message indicating that it is too heavy. If the object weighs less than 100 newtons, display a message indicating that it is too light.  '''

# Weight calculation based on mass
# Constants
GRAVITY = 9.8  # Gravitational acceleration in m/s^2

# Input: Ask the user to enter the mass of the object in kilograms
mass = float(input("Enter the object's mass in kilograms: "))

# Calculate the weight in newtons
weight = mass * GRAVITY

# Display the weight
print(f"The weight of the object is {weight:.2f} newtons.")

# Check if the weight is too heavy, too light, or within the normal range
if weight > 500:
    print("The object is too heavy.")
elif weight < 100:
    print("The object is too light.")
else:
    print("The object's weight is within the normal range.")
