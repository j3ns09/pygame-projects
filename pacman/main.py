import pygame

WIDTH, HEIGHT = 800, 800
COLS, ROWS = 21, 23
TITLE = "Pac-man"

w, h = WIDTH/COLS, HEIGHT/ROWS
w_offset = (w - w * 1.5) / 2

WALL_COLOR = (0, 0, 255)


screen = None
clock = None
running = False

# we now create the map of the walls,
# if 1 wall, if 0 not wall
# 21 columns // 23 rows
game_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1],
    [1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 2, 1, 2, 1, 2, 2, 2, 1, 2, 1, 2, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1],
    [1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1],
    [1, 1, 2, 2, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 2, 2, 1, 1],
    [1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
];

def setup():
    global screen, clock
    global running
    
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)
    
    clock = pygame.time.Clock()
    
    running = True

def update_input():
    global running
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_q, pygame.K_ESCAPE]:
                running = False

def update_gui():
    screen.fill("black")
    
    for i in range(COLS):
        for j in range(ROWS):
            tile = game_map[j][i]
            x = i * w
            y = j * h

            rect = pygame.Rect(x, y, w, h)

            match tile:
                case 1:
                    pygame.draw.rect(screen, WALL_COLOR, rect)

                    if (i > 0 and game_map[j][i - 1] == 1):
                        new_rect = pygame.Rect(rect.x + w_offset, rect.y + w_offset, rect.width - .5, rect.height - .5)
                        pygame.draw.rect(screen, "black", rect);

                    # if (j < map[0].length - 1 && map[i][j + 1] == 1) {
                    #     createRect(
                    #         j * oneBlockSize + wallOffset,
                    #         i * oneBlockSize + wallOffset,
                    #         wallSpaceWidth + wallOffset,
                    #         wallSpaceWidth,
                    #         wallInnerColor
                    #     );
                    # }

                    # if (i < map.length - 1 && map[i + 1][j] == 1) {
                    #     createRect(
                    #         j * oneBlockSize + wallOffset,
                    #         i * oneBlockSize + wallOffset,
                    #         wallSpaceWidth,
                    #         wallSpaceWidth + wallOffset,
                    #         wallInnerColor
                    #     );
                    # }

                    # if (i > 0 && map[i - 1][j] == 1) {
                    #     createRect(
                    #         j * oneBlockSize + wallOffset,
                    #         i * oneBlockSize,
                    #         wallSpaceWidth,
                    #         wallSpaceWidth + wallOffset,
                    #         wallInnerColor

    clock.tick(60)
    pygame.display.flip()

def update_logic():
    pass

def main():
    setup()

    while running:
        update_input()
        update_logic()
        update_gui()

if __name__ == "__main__":
    main()