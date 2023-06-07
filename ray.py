import math
import pygame

class Ray:
    def __init__(self, pos, angle):
        self.pos = pos
        self.dir = self.from_angle(angle)
        pass

    def from_angle(self, angle):
        return pygame.Vector2(math.cos(angle), math.sin(angle))

    def look_at(self, x, y):
        self.dir = pygame.Vector2(x, y) - self.pos
        self.dir.normalize()
        pass

    def draw(self, ds):
        pygame.draw.line(ds, (255, 255, 255), self.pos, self.dir * 10)
        pass

    def cast(self, wall):
        x1 = wall.a.x
        y1 = wall.a.y
        x2 = wall.b.x
        y2 = wall.b.y

        x3 = self.pos.x
        y3 = self.pos.y
        x4 = self.pos.x + self.dir.x
        y4 = self.pos.y + self.dir.y

        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if den == 0:
            return

        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den
        if t > 0 and t < 1 and u > 0:
            pt = pygame.Vector2()
            pt.x = x1 + t * (x2 - x1)
            pt.y = y1 + t * (y2 - y1)
            return pt
        else:
          return None
