from paddle import Paddle
from ball import Ball
import pygame

WIDTH, HEIGHT = 800, 600

score = 0


def setup():
    global screen, clock, running
    global mObjects

    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption("Pong")

    clock = pygame.time.Clock()
    running = True

    ball = Ball(WIDTH/2, HEIGHT/2, screen)
    player1 = Paddle(True, screen)
    player2 = Paddle(False, screen)

    mObjects = [ball, player1, player2]



def update_gui():
    global screen, clock
    global mObjects

    screen.fill("black")

    for obj in mObjects:
        obj.show()

    pygame.display.flip()
    clock.tick(60)

def update_logic():
    global mObjects

    for obj in mObjects:
        if isinstance(obj, Paddle):
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key ==
        else:
            obj.update()

def check_events():
    global running

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

def main():
    global running

    setup()

    while running:
        update_logic()
        update_gui()

        check_events()





if __name__ == "__main__":
    main()
