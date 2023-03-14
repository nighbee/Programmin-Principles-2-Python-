import pygame, sys
from pygame.locals import *
import random
pygame.init()
#fps
fps = 60
FramePerSec = pygame.time.Clock()
#colors
black= pygame.Color(0,0,0) #black
white= pygame.Color(255,255,255)
grey= pygame.Color(128,128,128)
red= pygame.Color(255,0,0)

#creating display
width=400
height=600
disp= pygame.display.set_mode((400,600))
disp.fill(white)
pygame.display.set_caption('Shit')

#classes of types
class enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('Enemy.png')
        self.rect=self.image.get_rect()
        self.rect.center=(random.randit(40, width-40), 0)

    def move(self):
        self.rect.move_ip(0,10)
        if(self.rect.bottom> 600):
            self.rect.top=0
            self.rect.center =(random.randit(30,370), 0)
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    def update(self):
        pressed_keys =pygame.key.get_pressed()
        if self.rect.left>0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5,0)
        if self.rect.right<=width:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5,0)
    def draw(self, surface):
        surface.blit(self.image, self.rect)

p1=player()
e1=enemy()

#game loop
while True:
    #shit
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    p1.update()
    e1.move()
    disp.fill(white)
    p1.draw(disp)
    e1.draw(disp)

    pygame.display.update()
    FramePerSec.tick(fps)

