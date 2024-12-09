''' Hot Dog Cookout Calculator
Assume hot dogs come in packages of 10, and hot dog buns come in packages of 8. Write a program that calculates the number of packages of hot dogs and the number of packages of hot dog buns needed for a cookout, with the minimum amount of leftovers. The program should ask the user for the number of people attending the cookout and the number of hot dogs each person will be given. The program should display the following details:
• The minimum number of packages of hot dogs required
• The minimum number of packages of hot dog buns required
• The number of hot dogs that will be left over
• The number of hot dog buns that will be left over '''

import math

# Input: Number of people and hot dogs per person
people = int(input("Enter the number of people attending the cookout: "))
hot_dogs_per_person = int(input("Enter the number of hot dogs each person will be given: "))

# Constants for package sizes
HOT_DOGS_PER_PACKAGE = 10
BUNS_PER_PACKAGE = 8

# Total number of hot dogs needed
total_hot_dogs = people * hot_dogs_per_person

# Calculate the number of packages needed
hot_dog_packages = math.ceil(total_hot_dogs / HOT_DOGS_PER_PACKAGE)
bun_packages = math.ceil(total_hot_dogs / BUNS_PER_PACKAGE)

# Calculate leftovers
leftover_hot_dogs = hot_dog_packages * HOT_DOGS_PER_PACKAGE - total_hot_dogs
leftover_buns = bun_packages * BUNS_PER_PACKAGE - total_hot_dogs

# Output the results
print(f"Minimum number of hot dog packages required: {hot_dog_packages}")
print(f"Minimum number of hot dog bun packages required: {bun_packages}")
print(f"Hot dogs left over: {leftover_hot_dogs}")
print(f"Buns left over: {leftover_buns}")
