''' Lap Times
Write a program that asks the user to enter the number of times that they have run around a racetrack, and then uses a loop to prompt them to enter the lap time for each of their laps. When the loop finishes, the program should display the time of their fastest lap, the time of their slowest lap, and their average lap time. ''' 

def lap_times():
    print("Lap Time Tracker\n")

    # Ask the user for the number of laps
    while True:
        try:
            num_laps = int(input("Enter the number of laps: "))
            if num_laps <= 0:
                print("The number of laps must be a positive integer. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Initialize variables to store lap times
    lap_times = []

    # Collect lap times
    for lap in range(1, num_laps + 1):
        while True:
            try:
                time = float(input(f"Enter the time for lap {lap} (in seconds): "))
                if time <= 0:
                    print("Lap time must be a positive number. Please try again.")
                else:
                    lap_times.append(time)
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    # Calculate fastest, slowest, and average lap times
    fastest_lap = min(lap_times)
    slowest_lap = max(lap_times)
    average_time = sum(lap_times) / num_laps

    # Display the results
    print("\nLap Time Results")
    print("-----------------")
    print(f"Fastest lap time: {fastest_lap:.2f} seconds")
    print(f"Slowest lap time: {slowest_lap:.2f} seconds")
    print(f"Average lap time: {average_time:.2f} seconds")

# Call the function
if __name__ == "__main__":
    lap_times()