import pygame

vec2 = pygame.math.Vector2

class Boundary:
    def __init__(self, x1, y1, x2, y2):
        self.a = vec2(x1, y1)
        self.b = vec2(x2, y2)
        self.screen : pygame.Surface | None = None

    def bind(self, screen):
        self.screen = screen

    def show(self):
        pygame.draw.line(self.screen, 'white', (self.a.x, self.a.y), (self.b.x, self.b.y))