import time
import turtle

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off screen updates

# Create the snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("white")
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"
snake_speed = 1
snake_length = 1

# Create the snake's body segments
segments = []

# Create the snake's food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Create the score display
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Score: 0", align="center", font=("Courier", 24, "normal"))


# Move the snake
def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)


# Function to check for collision with boundaries
def collision_with_boundaries():
    if snake.xcor() > 290 or snake.xcor() < -290 or snake.ycor() > 290 or snake.ycor() < -290:
        time.sleep(1)
        snake.goto(0, 0)
        snake.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the segments list
        segments.clear()

        # Reset the score
        score.clear()
        score.write("Score: 0", align="center", font=("Courier", 24, "normal"))

        # Reset the snake's length and speed
        global snake_speed
        global snake_length
        snake_speed = 1
        snake_length = 1


# Function to check for collision with food
def collision_with_food():
    if snake.distance(food) < 20:
        x = food.xcor()
        y = food.ycor()
        food.goto(x, y)

        # Create a new segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    # Increase the snake's length and speed
    global snake_speed
    global snake_length
    snake_speed += 0.1
    snake_length += 1

    # Update the score display
    score.clear()
    score.write("Score: {}".format(snake_length - 1), align="center", font=("Courier", 24, "normal"))

    wn.listen()
    wn.onkeypress(lambda: snake.direction("up"), "Up")
    wn.onkeypress(lambda: snake.direction("down"), "Down")
    wn.onkeypress(lambda: snake.direction("left"), "Left")
    wn.onkeypress(lambda: snake.direction("right"), "Right")

    while True:
        wn.update()


# Check for collision with boundaries
collision_with_boundaries()

# Check for collision with food
collision_with_food()

# Move the snake
move()

# Move the segments of the snake
for index in range(len(segments) - 1, 0, -1):
    x = segments[index - 1].xcor()
    y = segments[index - 1].ycor()
    segments[index].goto(x, y)

# Move the first segment of the snake to where the head is
if len(segments) > 0:
    x = snake.xcor()
    y = snake.ycor()
    segments[0].goto(x, y)

# Increase the snake's speed
time.sleep(snake_speed)
wn.mainloop()