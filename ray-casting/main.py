import pygame

from boundary import Boundary
from ray import Ray

# Constants
WIDTH, HEIGHT = 500, 500
TITLE = "Ray casting"

# Pygame variables
running = False
screen = None
clock = None

v_objects = []

def setup():
    global screen, clock
    global running

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    running = True

    wall = Boundary(400, 125, 400, 375)
    wall.bind(screen)

    ray = Ray(100, 250)
    ray.bind(screen)

    v_objects.append(wall)
    v_objects.append(ray)

def check_inputs():
    global running

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_ESCAPE, pygame.K_q):
                running = False

def update_gui():
    screen.fill('black')

    for obj in v_objects:
        obj.show()

    pygame.display.flip()


def main():
    setup()

    while running:
        check_inputs()

        update_gui()

if __name__ == '__main__':
    main()