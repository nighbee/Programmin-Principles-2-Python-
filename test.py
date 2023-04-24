import pygame
import time
import random
import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="snake_game",
    user="postgres",
    password="your_password"
)

# Create a cursor object
cur = conn.cursor()

# Create users table
cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE,
        level INTEGER DEFAULT 1
    )
''')
conn.commit()

# Create scores table
cur.execute('''
    CREATE TABLE IF NOT EXISTS scores (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users(id),
        score INTEGER,
        level INTEGER,
        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')
conn.commit()

# Close the cursor and database connection
cur.close()
conn.close()

# initialization
pygame.init()

# defining colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# defining screen
dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

# adjusting snake
snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# updating and showing ur score
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

# logic of snake when +1 fruit
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, white, [x[0], x[1], snake_block, snake_block])

# message showing
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# function to insert user into the database
def insert_user(username):
    conn = psycopg2.connect(
        database="snakeuser",
        user="postgres",
        password="72zv5u3xp"
    )
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    if user is None:
        cur.execute("INSERT INTO users (username) VALUES (%s)", (username,))
        conn.commit()
        cur.execute("SELECT id FROM users WHERE username = %s", (username,))
        user = cur.fetchone()
    cur.close()
    conn.close()
    return user[0]

# function to get user's current score from the database
def get_user_score(user_id):
    conn = psycopg2.connect(
        host="localhost",
        database="snake_game",
        user="postgres",
        password="your_password"
    )
    cur = conn.cursor()
    cur.execute("SELECT COALESCE(SUM(score), 0) FROM scores WHERE user_id = %s", (user_id,))
    user_score = cur.fetchone()[0]
    cur.close()
    conn.close()
    return user_score

# main gameloop
def gameLoop():
    game_over = False
    game_close = False

    # prompt user to enter their username
    username = input("Enter your username: ")
    user_id = insert_user(username)
    user_score = get_user_score(user_id)
    print(f"Welcome back, {username}! Your current score is {user_score}.")

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # random food spawn
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        # condition of game stop
        while game_close == True:
            dis.fill(black)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
            #paly again or not window
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # handling arrow keys
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # pause the game and save the current state and score to the database
                    cur_score = Length_of_snake - 1
                    cur.execute("INSERT INTO scores (user_id, score, level) VALUES (%s, %s, %s)", (user_id, cur_score, 1))
                    conn.commit()
                    print(f"Game paused. Your score has been saved to the database. Your current score is {Length_of_snake - 1}.")
                    while True:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                    print("Resuming game...")
                                    break
                        else:  # execute when the inner loop is not broken
                            continue
                        # execute when the inner loop is broken
                        break

            if keys[pygame.K_LEFT]:
                x1_change = -snake_block
                y1_change = 0
            elif keys[pygame.K_RIGHT]:
                x1_change = snake_block
                y1_change = 0
            elif keys[pygame.K_UP]:
                y1_change = -snake_block
                x1_change = 0
            elif keys[pygame.K_DOWN]:
                y1_change = snake_block
                x1_change = 0

        # hitting boundaries
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        # when the snake hits the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            print("Yummy!!")

        clock.tick(snake_speed)

    # closing pygame module
    pygame.quit()

# starting the game
gameLoop()

## all same records
pat_first_name= input("Enter ur search first name: ")
pat_last_name= input("Enter ur search last name: ")
pat_number= input("Enter number for search: ")
cur.execute("SELECT * FROM contacts where first_name LIKE %s OR last_name LIKE %s OR phone_number LIKE %s ", ('%s'+pat_first_name+'%s', '%s'+pat_last_name+'%s', '%s'+pat_number+'%s'))
s_rows= cur.fetchall()
for s_row in s_rows:
    print(f"{s_row[0]} - {s_row[1]} {s_row[2]}: {s_row[3]}")
