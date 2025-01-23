import pygame
import pygame.font as font

font.init()

class Node:
    def __init__(self, screen):
        self.screen = screen

        self.pos = pygame.Vector2()
        self.width = 50

        self.last_mouse_x = 0
        self.last_mouse_y = 0

        self.mouse_held = False
    
    def update(self):
        self.check_drag()
        self.show()
    
    def show(self):
        # Overriden by child classes
        pass

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