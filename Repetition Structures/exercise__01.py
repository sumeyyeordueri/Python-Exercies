''' Bug Collector
A bug collector collects bugs every day for five days. Write a program that keeps a running total of the number of bugs collected during the five days. The loop should ask for the number of bugs collected for each day, and when the loop is finished, the program should display the total number of bugs collected.'''

def bug_collector():
    total_bugs = 0  # Initialize total bugs counter
    
    print("Bug Collector Program\n")
    
    # Loop for 5 days
    for day in range(1, 6):
        while True:
            try:
                bugs = int(input(f"Enter the number of bugs collected on day {day}: "))
                if bugs < 0:
                    print("Number of bugs cannot be negative. Please try again.")
                else:
                    total_bugs += bugs
                    break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    print(f"\nTotal number of bugs collected over 5 days: {total_bugs}")

# Call the function
if __name__ == "__main__":
    bug_collector()
