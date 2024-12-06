'''Ingredient Adjuster
A cookie recipe calls for the following ingredients:
• 1.5 cups of sugar
• 1 cup of butter
• 2.75 cups of flour
The recipe produces 48 cookies with this amount of the ingredients. Write a program that asks the user how many cookies he or she wants to make, then displays the number of cups of each ingredient needed for the specified number of cookies.'''


# Define the base recipe
sugar_per_cookie = 1.5 / 48
butter_per_cookie = 1 / 48
flour_per_cookie = 2.75 / 48

# Ask the user how many cookies they want to make
desired_cookies = int(input("How many cookies do you want to make? "))

# Calculate the required ingredients
sugar_needed = sugar_per_cookie * desired_cookies
butter_needed = butter_per_cookie * desired_cookies
flour_needed = flour_per_cookie * desired_cookies

# Display the results
print(f"For {desired_cookies} cookies, you will need:")
print(f"- {sugar_needed:.2f} cups of sugar")
print(f"- {butter_needed:.2f} cups of butter")
print(f"- {flour_needed:.2f} cups of flour")
