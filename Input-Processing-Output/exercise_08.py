#8.Circle Measurements
#Write a program that asks the user to enter the radius of a circle. The program should cal- culate and display the area and circumference of the circle using πr2 for the area and 2πr for the circumference.
#Hint:Youcaneitheruse3.14159asthevalueofpi(π),oraddthestatement"import math" to the start of the program and then use "math.pi" wherever you need the value of pi in the program.

import math

# Ask the user to enter the radius of the circle
radius = float(input("Enter the radius of the circle: "))

# Calculate the area and circumference
area = math.pi * (radius ** 2)
circumference = 2 * math.pi * radius

# Display the results
print(f"The area of the circle is: {area:.2f}")
print(f"The circumference of the circle is: {circumference:.2f}")

