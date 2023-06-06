from cell import Cell
import random
import pygame

class MazeGenerator:
    def __init__(self, width, height, rows):
        self.width = width
        self.height = height
        self.rows = rows
        self.gridSize = self.width // self.rows

        self.grid = []
        self.stack = []

        self.create_maze()
        
        self.current = self.grid[0]
        self.current.visited = True

        self.done = False
        pass

    def create_maze(self):
        for i in range(self.rows):
            for j in range(self.rows):
                self.grid.append(Cell(i, j, self.gridSize))
        pass

    def index(self, i, j):
        if i < 0 or j < 0 or i > self.rows - 1 or j > self.rows - 1:
            return -9999
        return j + i * self.rows
    
    def check_neighbors(self, i, j):
        neighbors = []

        try:
            top = self.grid[self.index(i, j-1)]
        except:
            top = None
        try:
            right = self.grid[self.index(i+1, j)]
        except:
            right = None
        try:
            bottom = self.grid[self.index(i, j+1)]
        except:
            bottom = None
        try:
            left = self.grid[self.index(i-1, j)]
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

    def removeWalls(self, current, new):
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

    def draw(self, ds):
        # Draw as lines to easily to convert to ray hit targets
        w = 10
        WHITE = (255, 255, 255)
        pygame.draw.line(ds, WHITE, [0, 0], [self.width, 0], width=w)
        pygame.draw.line(ds, WHITE, [self.width, 0], [self.width, self.height], width=w)
        pygame.draw.line(ds, WHITE, [self.width, self.height], [0, self.height], width=w)
        pygame.draw.line(ds, WHITE, [0, self.height], [0, 0], width=w)

        for g in self.grid:
            g.draw(ds)

        if not self.done:
            self.current.highlight(ds)


    def step(self):
        if self.done:
            return True
        # Step 1
        new = self.check_neighbors(self.current.i, self.current.j)
        if new:
            new.visited = True
            # Step 2
            self.stack.append(new)

            # Step 3
            self.removeWalls(self.current, new)
            
            # Step 4
            self.current = new
        elif len(self.stack) > 0:
            self.current = self.stack.pop(-1)
        else:
            self.done = True

        return self.done
