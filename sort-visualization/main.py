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
    global maximum
    
    n = len(values)
    for i in range(n):
        random_num = random.randint(1, HEIGHT - 10)
        values[i] = Item(screen, random_num, i, n)
    maximum = max(values)

def setup():
    global screen, clock, running
    global pause
    
    pygame.init()

    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption("Sorting algorithms")
    clock = pygame.time.Clock()
    running = True
    pause = False

    gen_random_values()
    values[0].is_selected = True

def selection():
    n = len(values)

    for i in range(n - 1):
        max = values[i]
        
        for j in range(i + 1, n):
            min = values[j]

            if min < max:
                max = min
        
        max.show()    
        values[i], values[j] = values[j], values[i]

    print(values)

def update_gui():
    global screen, clock

    screen.fill((41, 41, 51))

    # for i in range(len(values)):
    #     values[i].update(i)
    #     values[i].show()

    selection()

    pygame.display.flip()
    clock.tick(60)

def update_logic():
    for i in range(1, len(values)):
        values[i], values[i-1] = values[i-1], values[i]

def check_events():
    global running
    global pause

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_q, pygame.K_ESCAPE):
                running = False
            if event.key == pygame.K_RETURN:
                pause = not pause
                gen_random_values()

def main():
    global running
    global pause

    setup()
    print(values)

    while running:
        if not pause:
            # update_logic()
            update_gui()

        check_events()



if __name__ == "__main__":
    main()
