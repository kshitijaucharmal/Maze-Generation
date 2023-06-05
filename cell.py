import pygame

class Cell:
    def __init__(self, i, j, size):
        self.i = i
        self.j = j
        self.size = size
        self.walls = [1, 1, 1, 1] # t, r, d, l (clockwise)

        self.visited = False

        self.visitedColor = (80, 80, 250)
        pass

    def draw(self, ds):
        x = self.i * self.size
        y = self.j * self.size
        w = self.size
        WHITE = (255, 255, 255)


        if self.visited:
            pygame.draw.rect(ds, self.visitedColor, (x, y, w, w))

        if self.walls[0]:
            pygame.draw.line(ds, WHITE, [x, y], [x + w, y])
        if self.walls[1]:
            pygame.draw.line(ds, WHITE, [x+w, y], [x + w, y+w])
        if self.walls[2]:
            pygame.draw.line(ds, WHITE, [x+w, y+w], [x, y+w])
        if self.walls[3]:
            pygame.draw.line(ds, WHITE, [x, y+w], [x, y])

        pass

    def highlight(self, ds):
        x = self.i * self.size
        y = self.j * self.size
        w = self.size
        WHITE = (255, 255, 255)
        pygame.draw.rect(ds, WHITE, (x, y, w, w))

