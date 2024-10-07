# 2.2.1. Create a function to use the turtle to draw an n-pointed star.
# Lines can intersect each other. Use this function to draw such star. 
# In description document include runtime screenshots of two examples with different n-values and describe your function. 
# Note: n is restricted to be an odd number.

import turtle

def star(n):
    if (n % 2 == 0) and (n > 0):
        return "The number of corners must be a positive odd number!"
    
    screen = turtle.Screen() 
    screen.bgcolor("white") 
    
    draw = turtle.Turtle()  # Initialize the turtle
    
    angle = 180 - (180 / n)  # Calculate the internal angle for the star
    
    # Draw the star
    for _ in range(n):
        draw.forward(300)  
        draw.right(angle)
    
    draw.hideturtle()  # Hide the turtle after drawing
    
    turtle.done()  # Keep the screen open

# Input to ask for the number of points
count = int(input("Enter the number of corners in the star: "))

star(count)