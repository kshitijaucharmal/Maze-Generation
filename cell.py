import pygame

class Cell:
    def __init__(self, i, j, size):
        self.i = i
        self.j = j
        self.size = size
        self.walls = [True, True] # T R

        self.visited = False

        self.visitedColor = (51, 51, 51)
        pass

    def draw(self, ds):
        x = self.i * self.size
        y = self.j * self.size
        w = self.size
        width = 2
        WHITE = (255, 255, 255)


        if self.walls[0]:
            pygame.draw.line(ds, WHITE, [x, y], [x + w, y], width=width)
        if self.walls[1]:
            pygame.draw.line(ds, WHITE, [x+w, y], [x + w, y+w], width=width)

        pass

    def highlight(self, ds):
        x = self.i * self.size
        y = self.j * self.size
        w = self.size
        WHITE = (255, 255, 255)
        pygame.draw.rect(ds, WHITE, (x, y, w, w))

