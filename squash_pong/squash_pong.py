import sys
import pygame

pygame.init()

FG_COLOUR = pygame.Color("white")
BG_COLOUR = pygame.Color("black")
WIDTH, HEIGHT = 1200, 800
SCREEN_SIZE = WIDTH, HEIGHT
BALL_SPEED = [-2, 2]
BORDER_WIDTH = PADDLE_WIDTH = 25
PADDLE_LENGTH = (HEIGHT - 2 * BORDER_WIDTH) * 0.25
BALL_RADIUS = 30
PADDING = 10

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Squash Pong")
screen.fill(BG_COLOUR)

ball = pygame.draw.circle(screen, 
                            FG_COLOUR, (
                            WIDTH - PADDING - PADDLE_WIDTH - BALL_RADIUS, 
                            HEIGHT/2), 
                            BALL_RADIUS)

paddle = pygame.draw.rect(screen,
                            FG_COLOUR,
                            (WIDTH - PADDLE_WIDTH - PADDING,
                            HEIGHT/2 - PADDLE_LENGTH/2,
                            PADDLE_WIDTH,
                            PADDLE_LENGTH))

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
    
    ball = ball.move(BALL_SPEED)
    if ball.left < BORDER_WIDTH or ball.right > WIDTH:
        BALL_SPEED[0] = -BALL_SPEED[0]
    if ball.top < BORDER_WIDTH or ball.bottom > (HEIGHT - BORDER_WIDTH):
        BALL_SPEED[1] = -BALL_SPEED[1]
    
    screen.fill(BG_COLOUR)
    screen.blit(ball, ball_rect)
    pygame.display.flip()