''' Turtle Graphics: Hit the Target Modification
Enhance the hit_the_target.py program that you saw in Program 3-9 so that, when the projectile misses the target, it displays hints to the user indicating whether the angle and/or the force value should be increased or decreased. For example, the program should display messages such as 'Try a greater angle' and 'Use less force.'''



import turtle
import math
import random

# Setup the screen
screen = turtle.Screen()
screen.title("Hit the Target")
screen.bgcolor("lightblue")

# Create a turtle for the projectile
projectile = turtle.Turtle()
projectile.shape("circle")
projectile.color("red")
projectile.penup()

# Create a turtle for the target
target = turtle.Turtle()
target.shape("circle")
target.color("green")
target.penup()

# Set the target's position
target.setposition(random.randint(200, 400), random.randint(-100, 100))

# Constants
GRAVITY = 9.8  # Gravitational acceleration in m/s^2
TARGET_RADIUS = 20  # Radius of the target

def fire_projectile(angle, force):
    # Convert angle to radians
    angle_rad = math.radians(angle)

    # Calculate initial velocity components
    initial_velocity_x = force * math.cos(angle_rad)
    initial_velocity_y = force * math.sin(angle_rad)

    # Time of flight
    time_of_flight = (2 * initial_velocity_y) / GRAVITY

    # Calculate projectile landing position
    distance = initial_velocity_x * time_of_flight
    height = initial_velocity_y * time_of_flight - (0.5 * GRAVITY * time_of_flight ** 2)

    return distance, height

def check_hit(target, distance, height):
    # Get the target's position
    target_x, target_y = target.position()

    # Check if the projectile is within the target's radius
    distance_to_target = math.sqrt((target_x - distance) ** 2 + (target_y - height) ** 2)

    if distance_to_target <= TARGET_RADIUS:
        return True
    return False

def give_hint(distance, height, target):
    target_x, target_y = target.position()
    
    if distance < target_x:
        print("Try a greater angle or more force.")
    elif distance > target_x:
        print("Try a smaller angle or less force.")

    if height < target_y:
        print("Use more force or a greater angle to reach the target height.")
    elif height > target_y:
        print("Use less force or a smaller angle to lower the trajectory.")

def main():
    angle = float(input("Enter the angle of the shot (in degrees): "))
    force = float(input("Enter the force of the shot (in m/s): "))

    distance, height = fire_projectile(angle, force)

    # Check if the shot hits the target
    if check_hit(target, distance, height):
        print("You hit the target!")
    else:
        print("You missed the target.")
        give_hint(distance, height, target)

# Run the program
main()

# Close the window when clicked
screen.exitonclick()
