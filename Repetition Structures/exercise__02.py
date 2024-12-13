''' Calories Burned
Running on a particular treadmill you burn 4.2 calories per minute. Write a program that uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30 minutes. '''

def calories_burned():
    # Calories burned per minute
    calories_per_minute = 4.2

    print("Calories Burned on the Treadmill\n")
    print("Minutes\tCalories Burned")
    print("-------------------------")

    # Loop through specified times
    for minutes in [10, 15, 20, 25, 30]:
        # Calculate calories burned
        calories = minutes * calories_per_minute
        # Display the result
        print(f"{minutes}\t{calories:.1f}")

# Call the function
if __name__ == "__main__":
    calories_burned()
