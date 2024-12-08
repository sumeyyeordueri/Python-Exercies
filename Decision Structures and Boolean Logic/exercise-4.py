''' Roman Numerals
Write a program that prompts the user to enter a number within the range of 1 through 10. The program should display the Roman numeral version of that number. If the number is outside the range of 1 through 10, the program should display an error message. The fol- lowing table shows the Roman numerals for the numbers 1 through 10:
 Number Roman Numeral
  1        I 
  2        II 
  3        III 
  4        IV 
  5        V 
  6        VI 
  7        VII 
  8        VIII 
  9        IX
  10       X           '''


# Input: Ask the user to enter a number
number = int(input("Enter a number (1-10): "))

# Define Roman numerals for numbers 1 through 10

roman_numerals = {
    1: "I", 2: "II", 3: "III", 4: "IV", 5: "V",
    6: "VI", 7: "VII", 8: "VIII", 9: "IX", 10: "X"
}

# Check if the number is within the valid range
if 1 <= number <= 10:
    print(f"The Roman numeral for {number} is {roman_numerals[number]}.")
else:
    print("Error: Please enter a number between 1 and 10.")


