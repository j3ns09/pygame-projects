import pygame

WIDTH, HEIGHT = 600, 600
TITLE = "Pendulum simulation"

running = False
screen = None
clock = None

# Pendulum bob radius
radius = 0

# Pendulum leader
lenght = 0
w = 0

def setup():
    global running
    global screen, clock
    global radius, w, lenght

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    running = True

    radius = 50
    w = 10
    lenght = HEIGHT//2

def update_gui():
    screen.fill('black')

    pygame.draw.rect(screen, 'white', pygame.Rect(WIDTH//2 - w//2, 0, w, lenght))
    pygame.draw.circle(screen, 'white', (WIDTH//2, HEIGHT//2), radius)


    pygame.display.flip()

def update_logic():
    pass

def check_inputs():
    global running

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key in {pygame.K_ESCAPE, pygame.K_q}:
                running = False



def main():
    setup()

    while running:
        check_inputs()

        update_logic()
        update_gui()

if __name__ == '__main__':
    main()