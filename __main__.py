import pygame
from maze_generator import MazeGenerator

WIDTH = 640
HEIGHT = 640
FPS = 60

ROWS = 16
gridSize = WIDTH // ROWS

ds = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Generation")
clock = pygame.time.Clock()

maze = MazeGenerator(WIDTH, HEIGHT, ROWS)

pos = pygame.Vector2(15, 15)

def main():
    run = True
    # done = False

    walls = maze.instant_maze()

    print("Total Walls:", len(walls))

    while run:
        ds.fill((11, 11, 11))

        # Drawing
        maze.draw(ds)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
        clock.tick(FPS)
        pass

if __name__ == "__main__":
    main()
