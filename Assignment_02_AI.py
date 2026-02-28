import pygame
import math


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


def make_grid(rows, width):
    grid = []
    gap = width // rows # Size of each square
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            # Create a Spot object for every coordinate
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)
    return grid

def draw_grid_lines(win, rows, width):
    gap = width // rows
    for i in range(rows):
        # Draw horizontal lines
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            # Draw vertical lines
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))

def draw(win, grid, rows, width):
    win.fill(WHITE) # Clear the screen every frame

    for row in grid:
        for spot in row:
            spot.draw(win) # Tell each spot to draw itself

    draw_grid_lines(win, rows, width)
    pygame.display.update() # "Flip" the drawing to the monitor


def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col

def main(win, width):
    rows = ROWS # Using the ROWS we got from input() earlier
    grid = make_grid(rows, width)

    start = None
    goal = None
    run = True

    while run:
        draw(win, grid, rows, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # LEFT CLICK
            if pygame.mouse.get_pressed()[0]: 
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, rows, width)
                spot = grid[row][col]
                
                if not start and spot != goal:
                    start = spot
                    start.make_start()
                elif not goal and spot != start:
                    goal = spot
                    goal.make_goal()
                elif spot != goal and spot != start:
                    spot.make_wall()

            # RIGHT CLICK (Reset)
            elif pygame.mouse.get_pressed()[2]: 
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, rows, width)
                spot = grid[row][col]
                spot.reset()
                if spot == start: start = None
                if spot == goal: goal = None

    pygame.quit()

# Call the function to start the app
main(WINDOW, WIDTH)