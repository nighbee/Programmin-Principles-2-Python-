import pygame
pygame.init()
screen_widht=640
screen_height=480
screen = pygame.display.set_mode((screen_height,screen_widht))
tracks=['first.mp3', 'second.mp3', 'third.mp3']
current_track=0
pygame.mixer.music.load(tracks[current_track])
running= True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        elif event.type == pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                current_track=(current_track-1)%len(tracks)
                pygame.mixermusic.load(tracks[current_track])
                pygame.mixer.music.play()
            elif event.key==pygame.K_RIGHT:
                current_track=(current_track+1)%len(tracks)
                pygame.mixer.music.load(tracks[current_track])
                pygame.mixer.music.play()


    screen.fill((255,255,255))
    pygame.display.flip()
pygame.quit()
