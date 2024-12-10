''' Roulette Wheel Colors
On a roulette wheel, the pockets are numbered from 0 to 36. The colors of the pockets are
as follows:
• Pocket 0 is green.
• For pockets 1 through 10, the odd-numbered pockets are red and the even-numbered
pockets are black.
• For pockets 11 through 18, the odd-numbered pockets are black and the even-numbered
pockets are red.
• For pockets 19 through 28, the odd-numbered pockets are red and the even-numbered
pockets are black.
• For pockets 29 through 36, the odd-numbered pockets are black and the even-numbered
pockets are red.
Write a program that asks the user to enter a pocket number and displays whether the pocket is green, red, or black. The program should display an error message if the user enters a number that is outside the range of 0 through 36. '''

# Input: Pocket number
pocket_number = int(input("Enter a pocket number (0-36): "))

# Determine the pocket color
if pocket_number < 0 or pocket_number > 36:
    print("Error: Invalid pocket number. Please enter a number between 0 and 36.")
elif pocket_number == 0:
    print("Pocket 0 is green.")
elif 1 <= pocket_number <= 10:
    if pocket_number % 2 == 0:
        print(f"Pocket {pocket_number} is black.")
    else:
        print(f"Pocket {pocket_number} is red.")
elif 11 <= pocket_number <= 18:
    if pocket_number % 2 == 0:
        print(f"Pocket {pocket_number} is red.")
    else:
        print(f"Pocket {pocket_number} is black.")
elif 19 <= pocket_number <= 28:
    if pocket_number % 2 == 0:
        print(f"Pocket {pocket_number} is black.")
    else:
        print(f"Pocket {pocket_number} is red.")
elif 29 <= pocket_number <= 36:
    if pocket_number % 2 == 0:
        print(f"Pocket {pocket_number} is red.")
    else:
        print(f"Pocket {pocket_number} is black.")

