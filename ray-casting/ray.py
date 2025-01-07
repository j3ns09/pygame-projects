from vec2 import vec2
import pygame

class Ray:
    def __init__(self, x, y):
        self.pos = vec2(x, y)
        self.dir = vec2(1, 0)
        self.screen : pygame.Surface | None = None

    def bind(self, screen):
        self.screen = screen

    def show(self):
        pygame.draw.line(self.screen, 'white', self.pos.unpack(), (self.pos + self.dir * 10).unpack())