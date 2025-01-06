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
<<<<<<< HEAD
            pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(self.x, self.y, width/(80), self.val))
=======
            pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(self.x, self.y, width/(80), self.val * 15 - 5))
>>>>>>> 2dd805f4525f2ac2a944f7a134d37bc3e6706d83
        else:
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.x, self.y, width/(80), self.val))

    def rev_select(self):
        self.is_selected = not self.is_selected

    def __gt__(self, other):
<<<<<<< HEAD
        return self.val > other.val if isinstance(other, Item) else Item.typeerror()

    def __lt__(self, other): return not self.__gt__(other)
=======
        if isinstance(other, Item):
            return self.val > other.val
>>>>>>> 2dd805f4525f2ac2a944f7a134d37bc3e6706d83

    def __repr__(self):
        return f"val={self.val}, pos={self.x, self.y}"
