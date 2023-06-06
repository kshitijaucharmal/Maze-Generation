import pygame
import random
from maze_generator import MazeGenerator
from cell import Cell

WIDTH = 600
HEIGHT = 600
FPS = 60

ROWS = 15
gridSize = WIDTH // ROWS

ds = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Generation")
clock = pygame.time.Clock()

maze = MazeGenerator(WIDTH, HEIGHT, ROWS)

def main():
    run = True
    done = False

    while not done or run:
        ds.fill((11, 11, 11))

        done = maze.step()

        maze.draw(ds)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
        clock.tick(FPS)
        pass

if __name__ == "__main__":
    main()
