import numpy as np
from random import uniform, choice
import pygame

class Ball:
    def __init__(self, x, y, window):
        self.x : float = x
        self.y : float = y
        self.r :int = 10
        self.dx : float = choice([uniform(-1, -2.5), uniform(1, 2.5)])
        self.dy : float = uniform(1, 2.5)

        self.window : pygame.Surface = window

    def initialize(self):
        self.x = 0
        self.y = 0

        self.dx = choice([uniform(-1, -2.5), uniform(1, 2.5)])
        self.dy = uniform(1, 2.5)

    def update(self):
        self.x += self.dx
        self.y += self.dy

        if self.y < 0 or self.y > self.window.get_height():
            self.dy *= -1

    def tap(self):
        self.dx += self.dx * 0.2
        self.dx *= -1

        print("ball speed:", round(np.sqrt(self.dx**2 + self.dy**2), 2), "px/f")
        print("x:", self.x, "y:", self.y)


    def show(self):
        pygame.draw.circle(self.window, (255,255,255), (self.x, self.y), self.r)
