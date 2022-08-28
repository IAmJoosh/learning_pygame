import sys
import pygame

# Initialises modules from pygame
pygame.init()

width, height = 320, 240
size = width, height
speed = [1, 1]
black = 0, 0, 0

# Create window
# Pygame represents images as Surface objects
# set_mode() creates new Surface that represents actual displayed graphics
screen = pygame.display.set_mode(size)

# Load image
# Supports bmp, jpg, png, tga, and gif
# load() returns Surface with ball data
# This surface will keep any colour key or alpha transparency from file
ball = pygame.image.load("intro_ball.gif")
# Rect represents rectangular area
ball_rect = ball.get_rect()

# Initialise program with infinite loop
while 1:
    # Check for user input
    for event in pygame.event.get():
        # If user input is clicking the X
        if event.type == pygame.QUIT:
            sys.exit()
    
    # Move ball
    ball_rect = ball_rect.move(speed)
    # Check that ball remains within bounds of window
    if ball_rect.left < 0 or ball_rect.right > width:
        speed[0] = -speed[0]
    if ball_rect.top < 0 or ball_rect.bottom > height:
        speed[1] = -speed[1]

    # Erase screen by covering in black. This gets rid of "old ball"
    screen.fill(black)
    # Draw "new ball"
    # blit refers to copying pixel colour from one image to another
    # blit() needs a surface to copy, and a postition on which to paste
    screen.blit(ball, ball_rect)
    # Make everything visible
    pygame.display.flip()