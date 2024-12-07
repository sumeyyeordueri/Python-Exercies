''' Planting Grapevines
A vineyard owner is planting several new rows of grapevines, and needs to know how many grapevines to plant in each row. She has determined that after measuring the length of a future row, she can use the following formula to calculate the number of vines that will fit in the row, along with the trellis end-post assemblies that will need to be constructed at each end of the row:
V= (R-2E) / S
The terms in the formula are:
V is the number of grapevines that will fit in the row.
R is the length of the row, in feet.
E is the amount of space, in feet, used by an end-post assembly. S is the space between vines, in feet.
Write a program that makes the calculation for the vineyard owner. The program should ask the user to input the following:
• The length of the row, in feet
• The amount of space used by an end-post assembly, in feet
• The amount of space between the vines, in feet
Once the input data has been entered, the program should calculate and display the num- ber of grapevines that will fit in the row.'''

# Input: Ask the user for the required values
row_length = float(input("Enter the length of the row (in feet): "))
end_post_space = float(input("Enter the amount of space used by an end-post assembly (in feet): "))
space_between_vines = float(input("Enter the space between vines (in feet): "))

# Calculation: Use the formula to calculate the number of vines
if space_between_vines <= 0 or (row_length - 2 * end_post_space) <= 0:
    print("Invalid input. Make sure the space between vines and row length are positive values.")
else:
    number_of_vines = (row_length - 2 * end_post_space) / space_between_vines

    # Output: Display the result
    print(f"The number of grapevines that will fit in the row is: {int(number_of_vines)}")
