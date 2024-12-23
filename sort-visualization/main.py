from item import Item
import numpy as np
import random
import pygame

WIDTH, HEIGHT = 800, 500

values = np.empty(8, dtype="O")
w = 10
c = 15
padding = 5
maximum = 0

def gen_random_values():
    global screen
    n = len(values)
    for i in range(n):
        random_num = random.randint(1, 100)
        values[i] = Item(screen, random_num, i, n)
    maximum = max(values)

def setup():
    global screen, clock, running
    pygame.init()

    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption("Sorting algorithms")
    clock = pygame.time.Clock()
    running = True

    gen_random_values()
    values[0].is_selected = True

    # print(values)

def update_gui():
    global screen, clock

    screen.fill((41, 41, 51))

    for i in range(len(values)):
        values[i].update(i)
        values[i].show()

#        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((i+1) * (WIDTH/(n + 1)), HEIGHT - values[i] * c - padding, w, values[i] * c - padding))

    pygame.display.flip()
    clock.tick(60)

def update_logic():
    for i in range(1, len(values)):
        values[i], values[i-1] = values[i-1], values[i]

def check_events():
    global running

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_q, pygame.K_ESCAPE):
                running = False

def main():
    global running

    setup()

    while running:
        # update_logic()
        update_gui()

        check_events()



if __name__ == "__main__":
    main()
