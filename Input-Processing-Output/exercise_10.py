''' Male and Female Percentages
Write a program that asks the user for the number of males and the number of females regis- tered in a class. The program should display the percentage of males and females in the class.
Hint: Suppose there are 8 males and 12 females in a class. There are 20 students in the class. The percentage of males can be calculated as 8 ÷ 20 = 0.4, or 40%. The percentage of females can be calculated as 12 ÷ 20 = 0.6, or 60%.'''

# Ask the user for the number of males and females
num_males = int(input("Enter the number of males in the class: "))
num_females = int(input("Enter the number of females in the class: "))

# Calculate the total number of students
total_students = num_males + num_females

# Calculate the percentages
male_percentage = (num_males / total_students) * 100
female_percentage = (num_females / total_students) * 100

# Display the results
print(f"Percentage of males: {male_percentage:.2f}%")
print(f"Percentage of females: {female_percentage:.2f}%")
