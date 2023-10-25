import turtle

# Create a turtle screen
screen = turtle.Screen()

# Create a turtle object
pen = turtle.Turtle()

def draw_square(side_length):
    """
    Draws a square using the turtle graphics module.
    :param side_length: Length of each side of the square.
    """
    for _ in range(4):
        pen.forward(side_length)
        pen.right(90)

while True:
    try:
        # Get user input for the side length of the square
        side_length = float(input("Enter the side length of the square (or type 'q' to quit): "))
        if side_length <= 0:
            print("Side length must be a positive number.")
            continue

        # Draw the square based on user input
        draw_square(side_length)
    except ValueError:
        user_input = input("Invalid input. Enter a number for side length or 'q' to quit: ")
        if user_input.lower() == 'q':
            break

# Close the window on click
screen.exitonclick()