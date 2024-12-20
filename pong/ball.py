import pygame

class Ball:
    def __init__(self, x, y, window):
        self.x : float = x
        self.y : float = y
        self.dx : float = 1
        self.dy : float = 4
        self.r :int = 10

        self.window : pygame.Surface = window

    def update(self):
        self.x += self.dx
        self.y += self.dy

        if self.y < 0 or self.y > self.window.get_height():
            self.dy *= -1

    def show(self):
        pygame.draw.circle(self.window, (255,255,255), (self.x, self.y), self.r)
