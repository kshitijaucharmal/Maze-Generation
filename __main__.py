import pygame
from maze_generator import MazeGenerator
from ray import Ray

WIDTH = 640
HEIGHT = 640
FPS = 60

ROWS = 16
gridSize = WIDTH // ROWS

ds = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Generation")
clock = pygame.time.Clock()

maze = MazeGenerator(WIDTH, HEIGHT, ROWS)

ray = Ray(pygame.Vector2(20, 20), 60)
pos = pygame.Vector2(ray.pos.x, ray.pos.y)

def main():
    run = True
    # done = False
    maze.instant_maze()

    while run:
        ds.fill((11, 11, 11))

        mouse_pos = pygame.Vector2(pygame.mouse.get_pos())

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            pos.y -= 1
        if keys[pygame.K_s]:
            pos.y += 1
        if keys[pygame.K_a]:
            pos.x -= 1
        if keys[pygame.K_d]:
            pos.x += 1

        ray.set(pos)
        ray.look_at(mouse_pos.x, mouse_pos.y)
        min_dist = 1000
        closest = None
        for b in maze.walls:
            p = ray.cast(b)
            if p:
                dist = ray.pos.distance_to(p)
                if dist < min_dist:
                    min_dist = dist
                    closest = p

        # Drawing
        maze.draw(ds)
        if closest:
            pygame.draw.line(ds, (255, 255, 0), ray.pos, closest)
            pygame.draw.circle(ds, (255, 0, 0), closest, 4)
        ray.draw(ds)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
        clock.tick(FPS)
        pass

if __name__ == "__main__":
    main()
