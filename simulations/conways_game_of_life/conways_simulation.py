from .cell import Cell 
from .prebuilds import place_glider, place_heavy_weight_spaceship_pattern

import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE
FPS = 10

# Colors
ALIVE_COLOR = (0, 255, 0)  # Green for alive cells
DEAD_COLOR = (0, 0, 0)     # Black for dead cells
GRID_COLOR = (50, 50, 50)  # Dark gray for grid lines

# Create the grid of cells
def create_grid():
    return [[Cell(x, y) for x in range(GRID_WIDTH)] for y in range(GRID_HEIGHT)]


# Count live neighbors
def count_live_neighbors(grid, x, y):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < GRID_WIDTH and 0 <= ny < GRID_HEIGHT and grid[ny][nx].is_alive:
            count += 1
    return count


# Update the grid based on Conway's rules
def update_grid(grid):
    new_grid = create_grid()
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            live_neighbors = count_live_neighbors(grid, x, y)
            if grid[y][x].is_alive:
                new_grid[y][x].is_alive = live_neighbors in (2, 3)
            else:
                new_grid[y][x].is_alive = live_neighbors == 3
    return new_grid


# Draw the grid
def draw_grid(screen, grid):
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            color = ALIVE_COLOR if grid[y][x].is_alive else DEAD_COLOR
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, GRID_COLOR, rect, 1)  # Draw grid lines


# Main function to run the game
def run():
    # Set up the display
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Conway's Game of Life")

    # Create the grid
    grid = create_grid()

    # Clock for controlling frame rate
    clock = pygame.time.Clock()

    running = True
    paused = True  # Start with the game paused
    grid = place_glider(grid, 2, 10)
    grid = place_glider(grid, 2, 20, flip_x=True)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused  # Toggle pause
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    # Toggle the state of the cell clicked
                    mx, my = pygame.mouse.get_pos()
                    x, y = mx // CELL_SIZE, my // CELL_SIZE
                    if 0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT:
                        grid[y][x].toggle_state()

        # Update the grid only if not paused
        if not paused:
            grid = update_grid(grid)

        # Draw everything
        screen.fill(DEAD_COLOR)  # Clear the screen
        draw_grid(screen, grid)
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

    # Quit Pygame
    pygame.quit()
    sys.exit()