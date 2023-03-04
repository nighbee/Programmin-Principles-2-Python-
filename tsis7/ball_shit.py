import pygame
pygame.init()
scr_width=640
scr_height=480
screen= pygame.display.set_mode((scr_width,scr_height))
b_size=50
b_color=(255, 0 ,0)
b_x=scr_width//2
b_y=scr_height//2
move_speed= 20
running= True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                b_y=max(b_y - move_speed,b_size//2)
            elif event.key == pygame.K_DOWN:
                b_y=min(b_y+move_speed, scr_height-b_size//2)
            elif event.key == pygame.K_LEFT:
                b_x=max(b_x-move_speed, b_size//2)
            elif event.key == pygame.K_RIGHT:
                b_x=min(b_x+move_speed, scr_width-b_size//2)
    screen.fill((255,255,255))
    pygame.draw.circle(screen, b_color, (b_x, b_y), b_size//2)
    pygame.display.flip()
pygame.quit()