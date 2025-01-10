import numpy as np
import pygame

# Alias
vec2 = pygame.math.Vector2

class Ray:
    def __init__(self, pos, angle):
        self.pos = pos
        self.dir = vec2(np.cos(angle), np.sin(angle))
        self.screen : pygame.Surface | None = None

    def bind(self, screen):
        self.screen = screen

    def cast(self, wall):
        x1, y1 = wall.a
        x2, y2 = wall.b

        x3, y3 = self.pos
        x4, y4 = self.pos - self.dir

        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

        if den == 0:
            return

        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
        u = ((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den

        if (t > 0 and t < 1 and u > 0):
            pt = vec2(x1 + t * (x2 - x1), y1 + t * (y2 - y1))
            return pt
        return


    def show(self):
        pygame.draw.line(self.screen, 'white', self.pos, self.pos + self.dir * 20)
