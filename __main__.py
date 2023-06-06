
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
        current.walls[3] = False
        new.walls[1] = False
    elif x == -1:
        current.walls[1] = False
        new.walls[3] = False
    y = current.j - new.j
    if y == 1:
        current.walls[0] = False
        new.walls[2] = False
    elif y == -1:
        current.walls[2] = False
        new.walls[0] = False

    pass

def main():
    run = True
    done = False

    current = grid[0]
    current.visited = True

    while run:
        ds.fill((11, 11, 11))

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

        for g in grid:
            g.draw(ds)

        if not done:
            current.highlight(ds)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
        clock.tick(FPS)
        pass

if __name__ == "__main__":
    main()
