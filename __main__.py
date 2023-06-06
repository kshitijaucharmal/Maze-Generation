
import pygame
import random
import numpy as np
from cell import Cell

WIDTH = 600
HEIGHT = 600
FPS = 60

ROWS = 15
gridSize = WIDTH // ROWS

ds = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Generation")
clock = pygame.time.Clock()

grid = []
stack = []

for i in range(ROWS):
    for j in range(ROWS):
        grid.append(Cell(i, j, gridSize))

def index(i, j):
    if i < 0 or j < 0 or i > ROWS - 1 or j > ROWS - 1:
        return -9999
    return j + i * ROWS

def check_neighbors(i, j):
    neighbors = []

    try:
        top = grid[index(i, j-1)]
    except:
        top = None
    try:
        right = grid[index(i+1, j)]
    except:
        right = None
    try:
        bottom = grid[index(i, j+1)]
    except:
        bottom = None
    try:
        left = grid[index(i-1, j)]
    except:
        left = None

    if top and not top.visited:
        neighbors.append(top)
    if right and not right.visited:
        neighbors.append(right)
    if bottom and not bottom.visited:
        neighbors.append(bottom)
    if left and not left.visited:
        neighbors.append(left)

    if len(neighbors) > 0:
        return random.choice(neighbors)
    else:
        return None

def removeWalls(current, new):
    x = current.i - new.i
    if x == 1:
        new.walls[1] = False
    elif x == -1:
        current.walls[1] = False
    y = current.j - new.j
    if y == 1:
        current.walls[0] = False
    elif y == -1:
        new.walls[0] = False

    pass

def draw():
    # Draw as lines to easily to convert to ray hit targets
    width = 10
    WHITE = (255, 255, 255)
    pygame.draw.line(ds, WHITE, [0, 0], [WIDTH, 0], width=width)
    pygame.draw.line(ds, WHITE, [WIDTH, 0], [WIDTH, HEIGHT], width=width)
    pygame.draw.line(ds, WHITE, [WIDTH, HEIGHT], [0, HEIGHT], width=width)
    pygame.draw.line(ds, WHITE, [0, HEIGHT], [0, 0], width=width)

    for g in grid:
        g.draw(ds)


def main():
    run = True
    done = False
    start = False

    current = grid[0]
    current.visited = True

    while run:
        ds.fill((11, 11, 11))

        if start:
            # Step 1
            new = check_neighbors(current.i, current.j)
            if new:
                new.visited = True
                # Step 2
                stack.append(new)

                # Step 3
                removeWalls(current, new)
                
                # Step 4
                current = new
            elif len(stack) > 0:
                current = stack.pop(-1)
            else:
                done = True

        draw()

        if not done:
            current.highlight(ds)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start = not start

        pygame.display.update()
        clock.tick(FPS)
        pass

if __name__ == "__main__":
    main()
