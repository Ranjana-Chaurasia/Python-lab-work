# Interactive Turtle Pattern Generator and Fractal Renderer
import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Pattern Generator")
screen.setup(width=800, height=600)

# User-defined background color
color = input("Enter background color (e.g., black, white, blue): ")
screen.bgcolor(color)

# Configure turtle pen
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)

# Function 1: Draw geometric pattern
def geometric_pattern():
    for i in range(36):
        for j in range(4):
            pen.forward(100)
            pen.right(90)
        pen.right(10)

# Function 2: Draw a spiral
def spiral():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    for i in range(150):
        pen.pencolor(colors[i % len(colors)])
        pen.forward(i * 2)
        pen.right(91)

# Function 3: Draw Koch snowflake recursively
def koch(length, depth):
    if depth == 0:
        pen.forward(length)
    else:
        for angle in [60, -120, 60, 0]:
            koch(length / 3, depth - 1)
            pen.left(angle)

def snowflake():
    for _ in range(3):
        koch(250, 3)
        pen.right(120)
        
while True:
    print("\n1. Geometric Pattern")
    print("2. Colorful Spiral")
    print("3. Koch Snowflake")
    print("4. Exit")

    choice = input("Choose a pattern: ")

    if choice == "4":
        break

    pen.clear()
    pen.penup()
    pen.goto(-100, 0)
    pen.pendown()
    pen.setheading(0)

    if choice == "1":
        geometric_pattern()
    elif choice == "2":
        spiral()
    elif choice == "3":
        snowflake()
    else:
        print("Invalid choice!")
        continue

    pen.hideturtle()

print("Pattern generator closed.")
screen.mainloop()