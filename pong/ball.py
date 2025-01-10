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
        self.x, self.y = map(lambda x: x * .5, self.window.get_size())

        self.dx = choice([uniform(-1, -2.5), uniform(1, 2.5)])
        self.dy = uniform(1, 2.5)

    def update(self):
        self.x += self.dx
        self.y += self.dy

        if self.y < 0 or self.y > self.window.get_height():
            self.dy *= -1

    def tap(self, paddle):
        speed = np.sqrt(self.dx**2 + self.dy**2)

        offset = (self.y + self.r - paddle.y) / (paddle.h + self.r)
        phi = 0.25 * np.pi * (2 * offset - 1)

        self.dx += self.dx * 0.2
        self.dx *= -1

        self.dy = speed * np.sin(phi)

    def show(self):
        pygame.draw.circle(self.window, (255,255,255), (self.x, self.y), self.r)
