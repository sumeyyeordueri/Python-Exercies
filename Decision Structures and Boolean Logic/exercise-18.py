''' Restaurant Selector

You have a group of friends coming to visit for your high school reunion, and you want to take them out to eat at a local restaurant. You aren’t sure if any of them have dietary restrictions, but your restaurant choices are as follows:
Joe’s Gourmet Burgers—Vegetarian: No, Vegan: No, Gluten-Free: No Main Street Pizza Company—Vegetarian: Yes, Vegan: No, Gluten-Free: Yes Corner Café—Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes
Mama’s Fine Italian—Vegetarian: Yes, Vegan: No, Gluten-Free: No
The Chef’s Kitchen—Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes
Write a program that asks whether any members of your party are vegetarian, vegan, or gluten-free, to which then displays only the restaurants to which you may take the group. Here is an example of the program’s output:
Is anyone in your party a vegetarian? yes Enter Is anyone in your party a vegan? no Enter
Is anyone in your party gluten-free? yes Enter Here are your restaurant choices:
Main Street Pizza Company Corner Cafe
The Chef's Kitchen
Here is another example of the program’s output:
Is anyone in your party a vegetarian? yes Enter Is anyone in your party a vegan? yes Enter
Is anyone in your party gluten-free? yes Enter Here are your restaurant choices:
Corner Cafe
The Chef's Kitchen  '''


def restaurant_selector():
    # Ask the user if anyone in the party is vegetarian, vegan, or gluten-free
    vegetarian = input("Is anyone in your party a vegetarian? (yes/no): ").strip().lower()
    vegan = input("Is anyone in your party a vegan? (yes/no): ").strip().lower()
    gluten_free = input("Is anyone in your party gluten-free? (yes/no): ").strip().lower()

    # List of restaurants and their dietary options
    restaurants = {
        "Joe’s Gourmet Burgers": {"vegetarian": False, "vegan": False, "gluten_free": False},
        "Main Street Pizza Company": {"vegetarian": True, "vegan": False, "gluten_free": True},
        "Corner Café": {"vegetarian": True, "vegan": True, "gluten_free": True},
        "Mama’s Fine Italian": {"vegetarian": True, "vegan": False, "gluten_free": False},
        "The Chef’s Kitchen": {"vegetarian": True, "vegan": True, "gluten_free": True},
    }

    # Filter the restaurants based on the dietary restrictions
    filtered_restaurants = []
    for restaurant, options in restaurants.items():
        if (vegetarian == "yes" and not options["vegetarian"]) or \
           (vegan == "yes" and not options["vegan"]) or \
           (gluten_free == "yes" and not options["gluten_free"]):
            continue
        filtered_restaurants.append(restaurant)

    # Display the filtered list of restaurants
    if filtered_restaurants:
        print("\nHere are your restaurant choices:")
        for restaurant in filtered_restaurants:
            print(restaurant)
    else:
        print("\nSorry, no restaurants match your dietary preferences.")

# Call the function to run the program
restaurant_selector()

