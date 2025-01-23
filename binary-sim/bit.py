import pygame
import pygame.font as font

from node import Node

class Bit(Node):
    def __init__(self, screen, val=0):
        super().__init__(screen)

        self.val = val
        self.pos = pygame.Vector2()
        self.width = 50

        self.font = font.SysFont("JetBrainsMonoNF-Regular", self.width)



    def show(self):
        rect = pygame.Rect(self.pos, (self.width, self.width))
        if self.val:
            pygame.draw.rect(self.screen, "green", rect)
        else:
            pygame.draw.rect(self.screen, "red", rect)
        
        text : pygame.Surface = self.font.render(str(self.val), False, "white")

        w, h = text.get_size()

        text_x_center, text_y_center = w / 2, h / 2

        self.screen.blit(text, (self.pos.x + (self.width - w) / 2, self.pos.y + (self.width - h) / 2))

    def check_drag(self):
        click = pygame.mouse.get_pressed()

        if not any(click):
            self.mouse_held = False
            return
        
        if click[0]:
            mouse_x, mouse_y = pygame.mouse.get_pos()            
            if self.pos.x <= mouse_x <= self.pos.x + self.width and self.pos.y <= mouse_y <= self.pos.y + self.width:
                if self.last_mouse_x != mouse_x or self.last_mouse_y != mouse_y:
                    self.pos.x = mouse_x - self.width / 2
                    self.pos.y = mouse_y - self.width / 2
        elif click[2]:
            if not self.mouse_held:
                if self.val:
                    self.val = 0
                else:
                    self.val = 1
                self.mouse_held = True
        elif click[1]:
            pass