import pygame
from maze_generator import MazeGenerator

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
    # done = False
    maze.instant_maze()

    while run:
        ds.fill((11, 11, 11))

        maze.draw(ds)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
        clock.tick(FPS)
        pass

if __name__ == "__main__":
    main()
