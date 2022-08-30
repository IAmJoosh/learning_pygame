import sys
import pygame
from objects import Ball, Paddle

pygame.init()

FG_COLOUR = pygame.Color("white")
BG_COLOUR = pygame.Color("black")
WIDTH, HEIGHT = 1200, 800
SCREEN_SIZE = WIDTH, HEIGHT
BALL_SPEED = [-2, 2]
PADDLE_SPEED = 0
BORDER_WIDTH = PADDLE_WIDTH = 25
PADDLE_LENGTH = (HEIGHT - 2 * BORDER_WIDTH) * 0.25
BALL_RADIUS = 30
PADDING = 10

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Squash Pong")
screen.fill(BG_COLOUR)

ball = Ball(WIDTH - PADDING - PADDLE_WIDTH - BALL_RADIUS, HEIGHT / 2, BALL_RADIUS, BALL_SPEED, FG_COLOUR)
ball.show(screen, FG_COLOUR)
# paddle = Paddle(WIDTH - PADDLE_WIDTH - PADDING, HEIGHT/2 - PADDLE_LENGTH/2, PADDLE_WIDTH, PADDLE_LENGTH, PADDLE_SPEED, FG_COLOUR)
# paddle.show(screen, FG_COLOUR)

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
    
    # if (ball.x - ball.radius) < BORDER_WIDTH or (ball.x + ball.radius) > (WIDTH):
    #     ball.speed[0] = -ball.speed[0]
    # if (ball.y - ball.radius) < BORDER_WIDTH or (ball.y + ball.radius) > (HEIGHT - BORDER_WIDTH):
    #     ball.speed[1] = -ball.speed[1]

    ball.update(screen, BG_COLOUR)

    pygame.display.flip()