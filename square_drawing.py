import turtle

# Create a turtle screen
window = turtle.Screen()

# Create a turtle object
t = turtle.Turtle()

# Draw a square
for _ in range(4):
    t.forward(100)  # Move forward by 100 units
    t.right(90)  # Turn right 90 degrees

# Close the window on click
window.exitonclick()