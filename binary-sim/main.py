import pygame

from bit import Bit

WIDTH, HEIGHT = 600, 600
TITLE = "Binary simulation"

running = False
screen = None
clock = None

nodes = []

def setup():
    global running
    global screen, clock

    pygame.font.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)

    clock = pygame.time.Clock()
    running = True

    nodes.append(Bit(screen))

def update_gui():
    screen.fill("black")

    for node in nodes:
        node.update()
    
    clock.tick(60)
    pygame.display.flip()

def update_logic():
    pass

def check_input():
    global running

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_q, pygame.K_ESCAPE]:
                running = False

def main():
    setup()

    while running:
        update_logic()
        update_gui()

        check_input()

if __name__ == "__main__":
    main()