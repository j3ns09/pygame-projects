import random
import pygame

from boundary import Boundary
from particle import Particle

# Constants
WIDTH, HEIGHT = 800, 800
TITLE = "Ray casting"

# Pygame variables
running = False
screen = None
clock = None

num_walls = 0

walls = []

wall = None
particle = None

def generate_walls(n):
    walls.clear()

    for i in range(num_walls):
        x1, y1 = random.randint(0, WIDTH), random.randint(0, HEIGHT)
        x2, y2 = random.randint(0, WIDTH), random.randint(0, HEIGHT)

        wall = Boundary(x1, y1, x2, y2)
        wall.bind(screen)
        walls.append(wall)

def setup():
    global screen, clock
    global running
    global num_walls, wall, particle

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    running = True

    num_walls = 4
    generate_walls(num_walls)
    
    particle = Particle()
    particle.bind(screen)

def check_inputs():
    global running

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_ESCAPE, pygame.K_q):
                running = False
            if event.key == pygame.K_r:
                generate_walls(num_walls)

def update_gui():
    screen.fill('black')

    for wall in walls:
        wall.show()

    particle.show()
    particle.look_at(walls)

    pygame.display.flip()
    clock.tick(60)

def update_logic():
    pass

def main():
    setup()

    while running:
        check_inputs()

        update_logic()
        update_gui()

if __name__ == '__main__':
    main()