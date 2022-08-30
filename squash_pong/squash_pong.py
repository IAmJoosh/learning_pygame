import sys
import pygame

pygame.init()

FG_COLOUR = pygame.Color("white")
BG_COLOUR = pygame.Color("black")
WIDTH, HEIGHT = 1200, 800
SCREEN_SIZE = WIDTH, HEIGHT
BALL_SPEED = [2, 2]
BORDER_WIDTH = 25
BALL_RADIUS = 30
PADDING = 50

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Squash Pong")
screen.fill(BG_COLOUR)

ball = pygame.draw.circle(screen, 
                            FG_COLOUR, (
                            WIDTH - BALL_RADIUS - PADDING, HEIGHT/2), 
                            BALL_RADIUS)

pygame.draw.rect(screen,
                    FG_COLOUR,
                    (0, 0, WIDTH, BORDER_WIDTH))

pygame.draw.rect(screen,
                    FG_COLOUR,
                    (0, HEIGHT - BORDER_WIDTH, WIDTH, BORDER_WIDTH))

pygame.draw.rect(screen,
                    FG_COLOUR,
                    (0, BORDER_WIDTH, BORDER_WIDTH, HEIGHT - 2 * BORDER_WIDTH))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()