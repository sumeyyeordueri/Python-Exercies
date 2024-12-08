'''  Areas of Rectangles
The area of a rectangle is the rectangle’s length times its width. Write a program that asks for the length and width of two rectangles. The program should tell the user which rectan- gle has the greater area, or if the areas are the same. '''

# Input: Ask the user for the length and width of the first rectangle
length1 = float(input("Enter the length of the first rectangle: "))
width1 = float(input("Enter the width of the first rectangle: "))

# Input: Ask the user for the length and width of the second rectangle
length2 = float(input("Enter the length of the second rectangle: "))
width2 = float(input("Enter the width of the second rectangle: "))

# Calculate the areas of the rectangles
area1 = length1 * width1
area2 = length2 * width2

# Compare the areas
if area1 > area2:
    print("The first rectangle has the greater area.")
elif area2 > area1:
    print("The second rectangle has the greater area.")
else:
    print("Both rectangles have the same area.")
