import numpy as np
import pygame

from spot import Spot

ROWS, COLUMNS = 100, 100

WIDTH : int = 750
HEIGHT : int = 750

w = WIDTH/COLUMNS
h = HEIGHT/ROWS

grid : np.ndarray = np.empty((ROWS,COLUMNS), dtype=Spot)

open_set : list[Spot] = []
closed_set : list[Spot] = []
path : list[Spot] = []

done : bool = False
no_solution : bool = False

def draw_spot(screen, rgb, spot):
    pygame.draw.rect(screen, rgb, pygame.Rect(spot.i*w, spot.j*h, w-1, h-1))

def heuristic(a: Spot, b: Spot):
    return b.i - a.i + b.j - a.j

def setup():
    global screen, running, clock
    global start, end

    # Pygame screen setup
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption("A* algorithm")
    clock = pygame.time.Clock()

    running = True

    for j in range(ROWS):
        for i in range(COLUMNS):
            grid[j, i] = Spot(i, j)

    for j in range(ROWS):
        for i in range(COLUMNS):
            grid[j, i].add_neighbours(grid)

    start = grid[0,0]
    end = grid[ROWS-1, COLUMNS-1]

    start.is_wall = False
    end.is_wall = False

    open_set.append(start)

def update_gui():
    global screen, running, clock
    global path

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(0, 0, WIDTH, HEIGHT))

    for j in range(ROWS):
        for i in range(COLUMNS):
            pygame.draw.rect(screen, (255,255,255), pygame.Rect(i*w, j*h, w-1, h-1))
            if grid[j, i].is_wall:
                pygame.draw.rect(screen, (0,0,0), pygame.Rect(i*w, j*h, w-1, h-1))


    for spot in closed_set:
        draw_spot(screen, (255, 0, 0), spot)

    for spot in open_set:
        draw_spot(screen, (0, 255, 0), spot)

    for spot in path:
        draw_spot(screen, (0, 0, 255), spot)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_q, pygame.K_ESCAPE]:
                running = False

    pygame.display.flip()
    clock.tick(60)

def update_logic():
    global open_set
    global path
    global done, no_solution

    if len(open_set) > 0 and not no_solution:
        lowest_index = 0
        for i in range(len(open_set)):
            if open_set[i].f < open_set[lowest_index].f:
                lowest_index = i

        current = open_set[lowest_index]

        if current == end:
            if not done:
                print("DONE")
                done = True
            return

        path = []
        temp = current
        path.append(temp)

        while temp.previous:
            path.append(temp.previous)
            temp = temp.previous


        open_set.pop(lowest_index)
        closed_set.append(current)

        neighbours = current.neighbours
        for neighbour in neighbours:
            if neighbour not in closed_set and not neighbour.is_wall:
                temp_g = current.g + 1
                new_path = False

                if neighbour in open_set:
                    if temp_g < neighbour.g:
                        neighbour.g = temp_g
                else:
                    neighbour.g = temp_g
                    new_path = True
                    open_set.append(neighbour)
                if new_path:
                    neighbour.h = heuristic(neighbour, end)
                    neighbour.f = neighbour.g + neighbour.h
                    neighbour.previous = current
    else:
        if not no_solution:
            print("No solution")
            no_solution = True
        else:
            return

def main():
    setup()

    while running:
        update_gui()
        update_logic()

if __name__ == "__main__":
    main()
