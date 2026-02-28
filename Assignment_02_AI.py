import pygame


WHITE = (255, 255, 255)   # Empty
BLACK = (0, 0, 0)         # Obstacle (Wall)
ORANGE = (255, 165, 0)    # Start Node
TURQUOISE = (64, 224, 208)# Goal Node
YELLOW = (255, 255, 0)    # Frontier (Priority Queue)
RED = (255, 0, 0)         # Visited/Expanded
GREEN = (0, 255, 0)       # Final Path
GREY = (128, 128, 128)    # Grid Lines

class Spot:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

   # Identify state by color
    def is_wall(self): return self.color == BLACK
    def is_start(self): return self.color == ORANGE
    def is_goal(self): return self.color == TURQUOISE

    def make_start(self): self.color = ORANGE
    def make_goal(self): self.color = TURQUOISE
    def make_wall(self): self.color = BLACK
    def make_visited(self): self.color = RED
    def make_frontier(self): self.color = YELLOW
    def make_path(self): self.color = GREEN
    def reset(self): self.color = WHITE

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))



def h(p1, p2, type="manhattan"):
    x1, y1 = p1
    x2, y2 = p2
    
    if type == "manhattan":
        # L1 Norm: Absolute horizontal + Absolute vertical distance
        return abs(x1 - x2) + abs(y1 - y2)
    else:
        # L2 Norm: Straight line distance (Pythagorean theorem)
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)