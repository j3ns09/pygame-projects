import pygame

class Paddle:
    def __init__(self, isleft, window):
        self.window : pygame.Surface = window
        self.isleft = isleft

        self.w : float = 10
        self.h : float = 70

        self.speed = 10

        if isleft:
            self.x : float = self.w / 2
        else:
            self.x : float = self.window.get_width() - self.w * 1.5

        self.y : float = self.window.get_height() / 2

    def update(self, ydir):
        self.y += self.speed * ydir


    def show(self):
        pygame.draw.rect(self.window, 'white', pygame.Rect(self.x, self.y, self.w, self.h))
