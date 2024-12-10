'''  Grade Calculator
A class has two tests worth 25 points each along with a main exam worth 50 points. For a stu- dent to pass the class, they must obtain an overall score of at least 50 points, and must obtain at least 25 points in the main exam. If a student’s total score is less than 50 or they obtain less than 25 points in the main exam, they receive a grade of “Fail”. Otherwise, their grade is as follows:
If they get more than 80, they get a grade of “Distinction”. 50–59 = “Pass”. If they get less than 80 but more than 60, they get a “Credit” grade.
If they get less than 60, they get a ”Pass” grade.
Write a program that prompts the user to enter their points for both tests and the exam and converts the values to integers. The program should first check if the points entered for the tests and exam are valid. If any of the test scores are not between 0 and 25, or the exam score is not between 0 and 50, the program should display an error message. Otherwise, the program should display the total points and the grade.   '''



# Input: Ask the user to enter scores for two tests and the main exam
test1 = int(input("Enter the score for Test 1 (0-25): "))
test2 = int(input("Enter the score for Test 2 (0-25): "))
exam = int(input("Enter the score for the Main Exam (0-50): "))

# Validate input
if not (0 <= test1 <= 25):
    print("Error: Test 1 score must be between 0 and 25.")
elif not (0 <= test2 <= 25):
    print("Error: Test 2 score must be between 0 and 25.")
elif not (0 <= exam <= 50):
    print("Error: Main Exam score must be between 0 and 50.")
else:
    # Calculate the total score
    total_score = test1 + test2 + exam

    # Determine the grade
    if total_score < 50 or exam < 25:
        grade = "Fail"
    elif total_score > 80:
        grade = "Distinction"
    elif 60 < total_score <= 80:
        grade = "Credit"
    elif 50 <= total_score <= 60:
        grade = "Pass"

    # Display the results
    print(f"Total Score: {total_score}")
    print(f"Grade: {grade}")
