import pygame
import math

# --- Configuration & User Input ---
WIDTH = 800
WIN = pygame.display.set_caption("A* Pathfinding Algorithm")

# Getting dynamic input before the window opens
try:
    ROWS = int(input("Enter the number of rows for your grid (e.g., 20, 50, 100): "))
except ValueError:
    ROWS = 50  # Fallback

# Initialize the window
WINDOW = pygame.display.set_mode((WIDTH, WIDTH))

def draw(win, grid, rows, width):
    win.fill((255, 255, 255)) # Fill background with white

    for row in grid:
        for spot in row:
            spot.draw(win) # Draws the color of the spot

    draw_grid_lines(win, rows, width) # Draws the grey lines
    pygame.display.update()

def main(win, width):
    grid = make_grid(ROWS, width)
    start = None
    end = None
    run = True

    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            
            # Logical mapping of mouse clicks goes here...
            
    pygame.quit()