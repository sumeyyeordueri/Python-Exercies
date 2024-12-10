''' Book Club Points
Serendipity Booksellers has a book club that awards points to its customers based on the number of books purchased each month. The points are awarded as follows:
• If a customer purchases 0 books, he or she earns 0 points.
• If a customer purchases 2 books, he or she earns 5 points.
• If a customer purchases 4 books, he or she earns 15 points.
• If a customer purchases 6 books, he or she earns 30 points.
• If a customer purchases 8 or more books, he or she earns 60 points.
Write a program that asks the user to enter the number of books that he or she has pur- chased this month, then displays the number of points awarded. '''

# Function to calculate points based on the number of books purchased
def calculate_points(books_purchased):
    if books_purchased == 0:
        return 0
    elif books_purchased == 2:
        return 5
    elif books_purchased == 4:
        return 15
    elif books_purchased == 6:
        return 30
    elif books_purchased >= 8:
        return 60
    else:
        return None  # Handle cases where books_purchased doesn't match criteria

# Main function
def main():
    print("Welcome to the Book Club Points Calculator!")

    # Get user input
    try:
        books = int(input("Enter the number of books you purchased this month: "))

        if books < 0:
            print("Error: The number of books cannot be negative.")
            return

        # Calculate points
        points = calculate_points(books)

        if points is not None:
            print(f"You purchased {books} books and earned {points} points.")
        else:
            print("Error: Invalid number of books entered.")

    except ValueError:
        print("Error: Please enter a valid integer for the number of books.")

# Run the program
main()
