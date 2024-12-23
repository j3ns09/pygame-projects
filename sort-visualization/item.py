import pygame
import math

class Item:
    def __init__(self, screen, val, i, n):
        self.screen : pygame.Surface = screen
        self.val = val

        self.__n = n

        self.x = (i+1) * (self.screen.get_width()/(n + 1))
        self.y = self.screen.get_height() - self.val * 15 - 5
        self.is_selected = False

    def update(self, i):
        self.x = (i+1) * (self.screen.get_width()/(self.__n + 1))

    def show(self, max=None):
        width, height = self.screen.get_size()

        if self.is_selected:
            pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(self.x, self.y, width/(80), math.log(self.val)))
        else:
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.x, self.y, width/(80), self.val * 15 - 5))

    def rev_select(self):
        self.is_selected = not self.is_selected

    def __repr__(self):
        return f"{self.x, self.y}"
