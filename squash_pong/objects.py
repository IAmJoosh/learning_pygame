import pygame
BORDER_WIDTH = 25
HEIGHT = 800
WIDTH = 1200

class Ball:
    def __init__(self, x, y, radius, speed, colour):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.colour = colour

    def show(self, screen, colour):
        pygame.draw.circle(screen, colour, (self.x, self.y), self.radius)


    def update(self, screen, hide_colour):

        newx = self.x + self.speed[0]
        newy = self.y + self.speed[1]

        if (newx - self.radius) < BORDER_WIDTH or (newx + self.radius) > WIDTH:
            self.speed[0] = -self.speed[0]
        elif (newy - self.radius) < BORDER_WIDTH or (newy + self.radius) > (HEIGHT - BORDER_WIDTH):
            self.speed[1] = -self.speed[1]
        else:
            self.show(screen, hide_colour)
            self.x += self.speed[0]
            self.y += self.speed[1]
            self.show(screen, self.colour)

class Paddle:
    def __init__(self, x, y, width, height, speed, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.colour = colour

    def show(self, screen, colour):
        pygame.draw.rect(screen, colour, (self.x, self.y, self.width, self.height))

    def update(self, screen, hide_colour):
        self.show(screen, hide_colour)
        self.y += self.speed
        self.show(screen, self.colour)