from paddle import Paddle
from ball import Ball
import pygame

WIDTH, HEIGHT = 800, 600

score = 0


def setup():
    global screen, clock, running
    global mObjects

    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption("Pong")

    clock = pygame.time.Clock()
    running = True

    ball = Ball(WIDTH/2, HEIGHT/2, screen)
    player1 = Paddle(True, screen)
    player2 = Paddle(False, screen)

    mObjects = {"ball" : ball,
                "p1" : player1,
                "p2" : player2
            }



def update_gui():
    global screen, clock
    global mObjects

    screen.fill("black")

    font = pygame.font.SysFont("cascadiacode", 36)

    ball, player1, player2 = mObjects.values()

    text_surface1 = font.render(str(player1.score), True, (255, 255, 255))
    text_surface2 = font.render(str(player2.score), True, (255, 255, 255))

    text_rect1 = text_surface1.get_rect(center=(20, 20))
    screen.blit(text_surface1, text_rect1)

    text_rect2 = text_surface2.get_rect(center=(WIDTH - 20, 20))
    screen.blit(text_surface2, text_rect2)

    ball.show(), player1.show(), player2.show()

    pygame.display.flip()
    clock.tick(60)

def update_logic():
    global screen
    global mObjects

    keys = pygame.key.get_pressed()

    ball, player1, player2 = mObjects.values()

    if ((player1.y + player1.h >= ball.y >= player1.y) and (ball.x - ball.r < player1.x + player1.w)) or ((player2.y + player2.h >= ball.y >= player2.y) and (ball.x + ball.r > player2.x)):
        ball.tap()

    if ball.x < 0:
        player2.score += 1
        ball.initialize()
    elif ball.x > screen.get_width():
        player1.score += 1
        ball.initialize()

    ball.update()

    if keys[pygame.K_UP]:
        player1.update(-1)
    elif keys[pygame.K_DOWN]:
        player1.update(1)

    if ball.y > player2.y + (player2.h / 2):
        player2.update(1)
    elif ball.y < player2.y + (player2.h / 2):
        player2.update(-1)


def check_events():
    global running

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

def debug():
    global clock
    print("FPS:", clock.get_fps())

def main():
    global running

    setup()

    while running:
        update_logic()
        update_gui()

        check_events()





if __name__ == "__main__":
    main()
