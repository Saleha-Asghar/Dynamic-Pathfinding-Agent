import pygame
import math
import random
from queue import PriorityQueue 

# --- 1. USER INPUT & CONFIGURATION ---
try:
    ROWS = int(input("Enter number of rows (e.g., 20, 50): "))
except ValueError:
    ROWS = 50

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("AI Pathfinding Agent - FAST NUCES")

# Assignment Colors
WHITE = (255, 255, 255)   # Empty
BLACK = (0, 0, 0)         # Wall
ORANGE = (255, 165, 0)    # Start
TURQUOISE = (64, 224, 208)# Goal
YELLOW = (255, 255, 0)    # Frontier
RED = (255, 0, 0)         # Visited
GREEN = (0, 255, 0)       # Path
GREY = (128, 128, 128)    # Grid Lines
CYAN = (0, 255, 255)

# --- 2. THE SPOT CLASS ---
class Spot:
    def __init__(self, row, col, width, total_rows):
        self.row, self.col = row, col
        self.x, self.y = row * width, col * width
        self.color = WHITE
        self.neighbors = []
        self.width, self.total_rows = width, total_rows
        self.g = float("inf")
        self.f = float("inf")
        self.parent = None

    def make_visited(self): self.color = CYAN
    def make_frontier(self): self.color = YELLOW
    def make_path(self): self.color = GREEN

    # This is required so the PriorityQueue can compare two spots
    def __lt__(self, other):
        return False

    def get_pos(self): return self.row, self.col
    def is_wall(self): return self.color == BLACK
    def reset(self): self.color = WHITE
    def make_start(self): self.color = ORANGE
    def make_goal(self): self.color = TURQUOISE
    def make_wall(self): self.color = BLACK
    def is_start(self): 
        return self.color == ORANGE

    def is_goal(self): 
        return self.color == TURQUOISE

    def is_wall(self): 
        return self.color == BLACK

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_wall(): # DOWN
            self.neighbors.append(grid[self.row + 1][self.col])
        if self.row > 0 and not grid[self.row - 1][self.col].is_wall(): # UP
            self.neighbors.append(grid[self.row - 1][self.col])
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_wall(): # RIGHT
            self.neighbors.append(grid[self.row][self.col + 1])
        if self.col > 0 and not grid[self.row][self.col - 1].is_wall(): # LEFT
            self.neighbors.append(grid[self.row][self.col - 1])

# --- 3. HELPER FUNCTIONS ---
def h(p1, p2): # Manhattan Distance
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            grid[i].append(Spot(i, j, gap, rows))
    return grid

def draw(win, grid, rows, width):
    win.fill(WHITE)
    for row in grid:
        for spot in row:
            spot.draw(win)
    
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        pygame.draw.line(win, GREY, (i * gap, 0), (i * gap, width))
    pygame.display.update()

def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    # Safety check: ensure the click stays within the list boundaries
    row = max(0, min(row, rows - 1))
    col = max(0, min(col, rows - 1))

    return row, col

def generate_random_map(grid, rows):
    for row in grid:
        for spot in row:
            # Clear existing walls but keep start/goal
            if not spot.is_start() and not spot.is_goal():
                spot.reset()
                # 30% probability of becoming a wall
                if random.random() < 0.3:
                    spot.make_wall()

def a_star(draw, grid, start, goal):
    count = 0
    open_set = PriorityQueue()
    # We put (f_score, tie_breaker, node) into the queue
    open_set.put((0, count, start))
    
    start.g = 0
    start.f = h(start.get_pos(), goal.get_pos())
    
    # Track which nodes are currently in the queue
    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # Get the node with the lowest f_score
        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == goal:
            # Reconstruct path by following parents
            temp = goal
            while temp.parent:
                temp = temp.parent
                if temp != start:
                    temp.make_path()
                draw()
            return True

        for neighbor in current.neighbors:
            temp_g_score = current.g + 1 # Distance between neighbors is 1

            if temp_g_score < neighbor.g:
                neighbor.parent = current
                neighbor.g = temp_g_score
                neighbor.f = temp_g_score + h(neighbor.get_pos(), goal.get_pos())
                
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((neighbor.f, count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_frontier()

        draw() # Update the visuals
        if current != start:
            current.make_visited()

    return False


def gbfs_algorithm(draw, grid, start, goal):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    start.f = h(start.get_pos(), goal.get_pos())
    open_set_hash = {start}
    visited = {start} # Use a set to track visited nodes for GBFS

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == goal:
            temp = goal
            while temp.parent:
                temp = temp.parent
                if temp != start:
                    temp.make_path()
                draw()
            return True

        for neighbor in current.neighbors:
            if neighbor not in visited:
                neighbor.parent = current
                f_score = h(neighbor.get_pos(), goal.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score, count, neighbor))
                    open_set_hash.add(neighbor)
                    visited.add(neighbor)
                    neighbor.make_frontier()

        draw()
        if current != start:
            current.make_visited()

    return False

# --- 4. MAIN LOOP ---
def main(win, width):
    grid = make_grid(ROWS, width)
    start = None
    goal = None
    run = True

    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]: # LEFT CLICK
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                if not start and spot != goal:
                    start = spot
                    start.make_start()
                elif not goal and spot != start:
                    goal = spot
                    goal.make_goal()
                elif spot != goal and spot != start:
                    spot.make_wall()

            elif pygame.mouse.get_pressed()[2]: # RIGHT CLICK
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                spot.reset()
                if spot == start: start = None
                if spot == goal: goal = None

            if event.type == pygame.KEYDOWN:
                # 1. Update neighbors for BOTH algorithms
                if (event.key == pygame.K_SPACE or event.key == pygame.K_g) and start and goal:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)

                # 2. Trigger A*
                if event.key == pygame.K_SPACE and start and goal:
                    a_star(lambda: draw(win, grid, ROWS, width), grid, start, goal)

                # 3. Trigger GBFS
                if event.key == pygame.K_g and start and goal:
                    gbfs_algorithm(lambda: draw(win, grid, ROWS, width), grid, start, goal)

                # 4. Map and Clear
                if event.key == pygame.K_r: 
                    generate_random_map(grid, ROWS)
                if event.key == pygame.K_c: 
                    start, goal = None, None
                    grid = make_grid(ROWS, width)
    pygame.quit()

main(WIN, WIDTH)