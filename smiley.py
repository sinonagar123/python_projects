import turtle  # Import the Turtle graphics library

# Create a Turtle object named 't'
t = turtle.Turtle()

# Set the fill color to yellow for filling the shapes
t.fillcolor('yellow')

# Begin filling the shape with the specified color
t.begin_fill()

# Draw a yellow circle with a radius of 100, creating the face of the smiley face
t.circle(100)

# End filling the shape
t.end_fill()

# Pen up to lift the pen from the canvas
t.penup()

# Move the turtle to the position (-40, 120) without drawing
t.goto(-40, 120)

# Pen down to start drawing again
t.pendown()

# Begin filling a circle with a radius of 10, creating the left eye
t.begin_fill()
t.circle(10)

# End filling the left eye
t.end_fill()

# Pen up to lift the pen
t.penup()

# Move the turtle to the position (40, 120) without drawing
t.goto(40, 120)

# Pen down to start drawing
t.pendown()

# Begin filling a circle with a radius of 10, creating the right eye
t.begin_fill()
t.circle(10)

# End filling the right eye
t.end_fill()

# Pen up to lift the pen
t.penup()

# Move the turtle to the position (0, 85) without drawing
t.goto(-30, 85)

# Pen down to start drawing
t.pendown()

# Rotate the turtle 90 degrees to the right
t.right(90)

# Draw a curved line to create the smile using a part of a circle with a radius of 50 and an angle of 85 degrees
t.circle(30, 190)

# Close the Turtle graphics window when you click on it
turtle.done()
