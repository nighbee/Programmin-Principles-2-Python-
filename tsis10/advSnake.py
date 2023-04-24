import pygame, random, psycopg2
from pygame import mixer

pygame.init()

# data
# Connect to the database
conn = psycopg2.connect(database="snakeuser", user="postgres", password="72zv5u3xp")
cur = conn.cursor()

# Create the contacts table
cur.execute("CREATE TABLE user (id SERIAL PRIMARY KEY, username VARCHAR(50) NOT NULL)")
cur.execute("CREATE TABLE user_score(id SERIAL PRIMARY KEY, user-id INTEGER NOT NULL, score INTEGER NOT NULL, FOREIGN KEY (user_id) REFERENCEuser(id) )" )

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

#adding levels
curr_level=1
levels=[i for i in range(100) if i%20]

#adjusting snake
snake_block = 10
snake_speed = 10

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 25)
level_font= pygame.font.SysFont("comicsansms", 25)


#updating and showing ur score
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


# level class
def user_level(curr_level):
    value= level_font.render("Your Level: "+ str(curr_level), True, yellow)
    dis.blit(value, [dis_width-10, 0])

# logic of snake when +1 fruit
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, white, [x[0], x[1], snake_block, snake_block])

#message showing
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

#NEW
#saving score
def save_score(user_id, score):
    cur.execute("INSERT INTO user_score (user_id, score) VALUES (%s,%s)", (user_id, score))
    conn.commit()
#getting user shit
def get_user(username):
    cur.execute("SELECT id FROM user WHERE username=%s", (username,))
    user= cur.fetchone()
    return user
#get user score
def get_user_score(user_id):
    cur.execute("SELECT score ROM user_score WHERE user_id=%s", (user_id,))
    user_score=cur.fetchone()
    return user_score

# main gameloop
def gameLoop():

    #username ask
    username=input("Enter ur username: ")
    # checking if user exists in database
    cur.execute("SELECT id, current_level FROM user WHERE username=%s", username)
    result=cur.fetchone()

    if result:
        user_id, current_level= result
        print("Welcome back, " + username+"!")
        print("Ur result is: "+str(current_level))
    else:
        cur.execute("INSERT INTO user (username, current_level) VALUES (%s, 1)", (username, ))
        conn.commit()
        user_id=cur.lastrowid
        print("welcome, "+username+"!")
        print("Your current level is 1")
        current_level=1

    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    #random food spawn
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    poisonx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    poisony = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

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
        #main loop logick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                mixer.music.stop()
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
        #logic of game ever
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        if Length_of_snake<1:
            game_close= True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        weight=[1,2,3]
        food_weight= random.choice(weight)
        if food_weight==1:
            pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        elif food_weight==2:
            pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
        elif food_weight==3:
            pygame.draw.rect(dis, yellow, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
#shit not workin
        # for x in snake_List[:-1]:
        #     if x == snake_Head:
        #         game_close = True
        # for level in levels:
        #     if Length_of_snake>= 20:
        #         snake_speed=12
        #     elif Length_of_snake>=40:
        #         snake_speed=15
        #     elif Length_of_snake>=60:
        #         snake_speed=17
        #     elif Length_of_snake>=80:
        #         snake_speed=20

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            if food_weight==1:
                Length_of_snake += 1
            elif food_weight==2:
                Length_of_snake+=2
            elif food_weight==3:
                Length_of_snake+=3
        elif x1==poisonx and y1== poisony:
            poisonx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            poisony = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake -=1
            our_snake(snake_block, snake_List)
        clock.tick(snake_speed)

    conn.autocommit=True
    cur.close()
    conn.close()
    pygame.quit()
    quit()


gameLoop()