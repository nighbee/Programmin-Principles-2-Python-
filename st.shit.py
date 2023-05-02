import pygame
import time
import random, psycopg2
# initialization
pygame.init()

#difining colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

#defining screen
dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

#adjusting snake
snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

#data
conn = psycopg2.connect(
    database= "snakeuser",
    user= "postgres",
    password= "72zv5u3xp"
)
# creating cursor
cur= conn.cursor()

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
        score TEXT
    )
''')
conn.commit()

# cur.execute("""
#     CREATE TABLE IF NOT EXISTS position (
#     id SERIAL PRIMARY KEY,
#     user_id INTEGER REFERENCES user(id),
#     snake_pos TEXT
#     )""")
# conn.commit()


#inserting user
def insert_user(username):
    cur.execute("SELECT id FROM users WHERE username =%s", (username, ))
    user=cur.fetchone()
    if user is None:
        cur.execute("INSERT INTO users (username) VALUES (%s)", (username,))
        conn.commit()
        cur.execute("SELECT id FROM users WHERE username = %s", (username,))
        user=cur.fetchone()
    return user[0]

def get_user_score(user_id):
    cur.execute("SELECT COALESCE(SUM(score), 0) FROM scores WHERE user_id =%s", (user_id,) )
    user_score=cur.fetchone()[0]
    return user_score

#updating and showing ur score
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

# logic of snake when +1 fruit
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, white, [x[0], x[1], snake_block, snake_block])

#message showing
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# #saving block positions
# def save_positions(snake_block, food_position):
#     snake_block_str=",".join([f"{block[0]}, {block[1]}" for block in snake_list])
# main gameloop
def gameLoop():
    game_over = False
    game_close = False

    username= input("enter username: ")
    user_id=insert_user(username)
    userscore = get_user_score(user_id)
    print(f"welcome back, {username}! Ur current score is {str(userscore)}")

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    #random food spawn
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        # condition of game stop
        while game_close == True:
            dis.fill(black)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            # cur.execute("INSERT INTO users (username) VALUES =%s", (username,))
            # conn.commit()
            game_end_score=Length_of_snake-1
            if userscore < game_end_score:
                cur.execute("INSERT INTO scores (user_id, score) VALUES (%s,%s)", (user_id, str(game_end_score)))
                conn.commit()

            pygame.display.update()
            #paly again or not window
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        #main loop logick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                elif event.key== pygame.K_SPACE:
                    cur_score=Length_of_snake-1
                    cur.execute("INSERT INTO scores (user_id, score) VALUES (%s,%s)", (user_id,str(cur_score)))
                    conn.commit()
                    print(f"Game paused, current score committed in database")
                    while True:
                        for event in pygame.event.get():
                            if event.type==pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    print("Resuming game...")
                                    break
                        else:
                            continue
                        break
                    # if game_close is False:
                    #     cur.execute("INSERT INTO position (user_id, snake_pos) VALUES (%s, %s, %s)", (user_id, snake_List ))
                    #     conn.commit()


        #logic of game ever
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        weight=[1,2,3]
        food_weight=random.choice(weight)
        if food_weight==1:
            pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        elif food_weight==2:
            pygame.draw.rect(dis, blue, [foodx,foody,snake_block,snake_block])
        elif food_weight==3:
            pygame.draw.rect(dis, yellow, [foodx, foody, snake_block, snake_block])
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

        #walls
        num_walls=10
        walls=[]
        for i in range(num_walls):
            wallx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            wally = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            walls.append((wallx, wally))

        if snake_Head in walls:
            game_over=True


        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            if food_weight==1:
                Length_of_snake += 1
            elif food_weight==2:
                Length_of_snake+=2
            elif food_weight==3:
                Length_of_snake+=3

        clock.tick(snake_speed)

    cur.close()
    conn.close()
    pygame.quit()
    quit()


gameLoop()