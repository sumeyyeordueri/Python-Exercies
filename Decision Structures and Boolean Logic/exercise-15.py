'''  Time Calculator
Write a program that asks the user to enter a number of seconds and works as follows:
• There are 60 seconds in a minute. If the number of seconds entered by the user is greater than or equal to 60, the program should convert the number of seconds to minutes and seconds.
• There are 3,600 seconds in an hour. If the number of seconds entered by the user is greater than or equal to 3,600, the program should convert the number of seconds to hours, minutes, and seconds.
• There are 86,400 seconds in a day. If the number of seconds entered by the user is greater than or equal to 86,400, the program should convert the number of seconds to days, hours, minutes, and seconds.'''



def time_calculator():
    """Convert seconds into days, hours, minutes, and seconds."""
    try:
        # Ask the user for the number of seconds
        total_seconds = int(input("Enter the number of seconds: "))

        if total_seconds < 0:
            print("Please enter a non-negative number of seconds.")
            return

        # Calculate days, hours, minutes, and seconds
        days = total_seconds // 86400
        remaining_seconds = total_seconds % 86400

        hours = remaining_seconds // 3600
        remaining_seconds %= 3600

        minutes = remaining_seconds // 60
        seconds = remaining_seconds % 60

        # Display the result
        if total_seconds >= 86400:
            print(f"{total_seconds} seconds is equal to {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds.")
        elif total_seconds >= 3600:
            print(f"{total_seconds} seconds is equal to {hours} hours, {minutes} minutes, and {seconds} seconds.")
        elif total_seconds >= 60:
            print(f"{total_seconds} seconds is equal to {minutes} minutes and {seconds} seconds.")
        else:
            print(f"{total_seconds} seconds is equal to {seconds} seconds.")

    except ValueError:
        print("Invalid input. Please enter an integer value.")

if __name__ == "__main__":
    time_calculator()


