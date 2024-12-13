''' Distance Traveled

The distance a vehicle travels can be calculated as follows:
distance 5 speed 3 time
For example, if a train travels 40 miles per hour for three hours, the distance traveled is 120 miles. Write a program that asks the user for the speed of a vehicle (in miles per hour) and the number of hours it has traveled. It should then use a loop to display the distance the vehicle has traveled for each hour of that time period. Here is an example of the desired output:
What is the speed of the vehicle in mph? 40 Enter How many hours has it traveled? 3 Enter
Hour         Distance Traveled
1                    40
2                    80
3                   120  '''


def distance_traveled():
    print("Distance Traveled Calculator\n")

    # Ask the user for the speed of the vehicle
    while True:
        try:
            speed = float(input("What is the speed of the vehicle in mph? "))
            if speed <= 0:
                print("Speed must be a positive number. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Ask the user for the number of hours traveled
    while True:
        try:
            hours = int(input("How many hours has it traveled? "))
            if hours <= 0:
                print("The number of hours must be a positive integer. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Display the header
    print("\nHour\tDistance Traveled")
    print("-------------------------")

    # Calculate and display the distance for each hour
    for hour in range(1, hours + 1):
        distance = speed * hour
        print(f"{hour}\t{distance:.2f}")

# Call the function
if __name__ == "__main__":
    distance_traveled()
