import numpy as np
import pygame

from ray import Ray

vec2 = pygame.math.Vector2

class Particle:
    def __init__(self):
        self.pos = vec2(250,250)
        self.rays = []
        self.screen : pygame.Surface | None = None

        for i in range(36):
            degrees = i * 10

            self.rays.append(Ray(self.pos, degrees * np.pi / 180))

    def bind(self, screen):
        self.screen = screen
        for ray in self.rays:
            ray.bind(screen)

    def look_at(self, walls: list):
        for ray in self.rays:
            closest = None
            record = float('inf')
            for wall in walls:
                pt = ray.cast(wall)

                if pt is not None:
                    d = self.pos.distance_to(pt)
                    if d < record:
                        record = d
                        closest = pt
            if closest is not None:
                pygame.draw.line(self.screen, 'white', ray.pos, closest)

    def update_position(self):
        mouse_pos = pygame.mouse.get_pos()
        self.pos = vec2(*mouse_pos)
        for ray in self.rays:
            ray.pos = self.pos

    def show(self):
        self.update_position()
        pygame.draw.circle(self.screen, 'white', self.pos, 10)

        for ray in self.rays:
            ray.show()