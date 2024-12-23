import pygame

class Paddle:
    def __init__(self, isleft, window):
        self.window : pygame.Surface = window
        self.isleft = isleft
        self.score = 0

        self.w : float = 10
        self.h : float = 70

        self.speed = 5

        if isleft:
            self.x : float = self.w / 2
        else:
            self.x : float = self.window.get_width() - self.w * 1.5

        self.y : float = self.window.get_height() / 2

    def update(self, ydir):
        dy = self.speed * ydir

        if self.y + dy > self.window.get_height() - self.h or self.y + dy < 0:
            return

        self.y += self.speed * ydir



    def show(self):
        pygame.draw.rect(self.window, 'white', pygame.Rect(self.x, self.y, self.w, self.h))
