'''  Magic Dates
The date June 10, 1960, is special because when it is written in the following format, the month times the day equals the year:
6/10/60
Design a program that asks the user to enter a month (in numeric form), a day, and a two- digit year. The program should then determine whether the month times the day equals the year. If so, it should display a message saying the date is magic. Otherwise, it should display a message saying the date is not magic. '''

# Input: Ask the user to enter the month, day, and year
month = int(input("Enter the month (in numeric form, e.g., 6 for June): "))
day = int(input("Enter the day: "))
year = int(input("Enter the year (as a two-digit number, e.g., 60 for 1960): "))

# Check if the date is magic
if month * day == year:
    print(f"The date {month}/{day}/{year} is magic!")
else:
    print(f"The date {month}/{day}/{year} is not magic.")
