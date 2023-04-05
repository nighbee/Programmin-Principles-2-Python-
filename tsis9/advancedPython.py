import pygame

# Initialize Pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (255, 192, 203)

# Set the screen dimensions
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the font for the buttons
button_font = pygame.font.SysFont('calibri', 16)

# Define the brush color
brush_color = BLACK

# Set the brush size
brush_size = 10

# Create the color buttons
color_buttons = [
    {
        'color': BLUE,
        'rect': pygame.Rect(10, 10, 50, 50)
    },
    {
        'color': RED,
        'rect': pygame.Rect(70, 10, 50, 50)
    },
    {
        'color': BLACK,
        'rect': pygame.Rect(130, 10, 50, 50)
    },
    {
        'color': WHITE,
        'rect': pygame.Rect(190, 10, 50, 50)
    },
    {
        'color': PINK,
        'rect': pygame.Rect(250, 10, 50, 50)
    }
]

# Define the eraser button
eraser_button = pygame.Rect(310, 10, 50, 50)

# Set the program loop
running = True
while running:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Change brush color on color button click
            for button in color_buttons:
                if button['rect'].collidepoint(event.pos):
                    brush_color = button['color']
            # Clear the screen on eraser button click
            if eraser_button.collidepoint(event.pos):
                screen.fill(BLACK)
        elif event.type == pygame.MOUSEMOTION:
            # Draw with the brush on mouse motion
            if pygame.mouse.get_pressed()[0]:
                pygame.draw.circle(screen, brush_color, event.pos, brush_size)
    # Draw the color buttons
    for button in color_buttons:
        pygame.draw.rect(screen, button['color'], button['rect'])
    # Draw the eraser button
    pygame.draw.rect(screen, RED, eraser_button)
    # Draw the "Erase" text on the eraser button
    erase_text = button_font.render("Erase", True, WHITE)
    erase_text_rect = erase_text.get_rect(center=eraser_button.center)
    screen.blit(erase_text, erase_text_rect)
    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
