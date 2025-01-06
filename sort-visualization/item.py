import pygame
import math

padding = 10

class Item:
    def typerror():
       raise TypeError("Not the right type for operand")
    
    def __init__(self, screen, val, i, n):
        self.screen : pygame.Surface = screen
        self.val = val

        self.__n = n

        self.x = (i+1) * (self.screen.get_width()/(n + 1))
        self.y = self.screen.get_height() - self.val - padding
        self.is_selected = False

    def update(self, i):
        self.x = (i+1) * (self.screen.get_width()/(self.__n + 1))

    def show(self, max=None):
        width, height = self.screen.get_size()

        if self.is_selected:
            pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(self.x, self.y, width/(80), self.val))
        else:
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.x, self.y, width/(80), self.val))

    def rev_select(self):
        self.is_selected = not self.is_selected

    def __gt__(self, other):
        return self.val > other.val if isinstance(other, Item) else Item.typeerror()

    def __lt__(self, other): return not self.__gt__(other)

    def __repr__(self):
        return f"val={self.val}, pos={self.x, self.y}"
