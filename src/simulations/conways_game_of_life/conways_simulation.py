import pygame
import sys
from .cell import Cell
from .prebuilds import place_glider, place_heavy_weight_spaceship_pattern

# Initialize Pygame
pygame.init()

# Constants
FPS = 10

# Colors
ALIVE_COLOR = (0, 255, 0)  # Green for alive cells
DEAD_COLOR = (0, 0, 0)  # Black for dead cells
GRID_COLOR = (50, 50, 50)  # Dark gray for grid lines


# Create the grid of cells
def create_grid(grid_width, grid_height, cell_size):
    return [[Cell(x, y) for x in range(grid_width)] for y in range(grid_height)]


# Count live neighbors
def count_live_neighbors(grid, x, y):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and grid[ny][nx].is_alive:
            count += 1
    return count


# Update the grid based on Conway's rules
def update_grid(grid):
    grid_width = len(grid[0])
    grid_height = len(grid)
    new_grid = create_grid(grid_width, grid_height, 20)
    for y in range(grid_height):
        for x in range(grid_width):
            live_neighbors = count_live_neighbors(grid, x, y)
            if grid[y][x].is_alive:
                new_grid[y][x].is_alive = live_neighbors in (2, 3)
            else:
                new_grid[y][x].is_alive = live_neighbors == 3
    return new_grid


# Draw the grid
def draw_grid(screen, grid, cell_size, offset_x, offset_y):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            rect = pygame.Rect((x * cell_size) + offset_x, (y * cell_size) + offset_y, cell_size, cell_size)
            color = ALIVE_COLOR if grid[y][x].is_alive else DEAD_COLOR
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, GRID_COLOR, rect, 1)  # Draw grid lines


# Main function to run the game
def run():
    # Initial window size
    width, height = 1800, 1000
    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
    pygame.display.set_caption("Conway's Game of Life")

    # Initial cell size
    cell_size = 40
    grid_width = width // cell_size
    grid_height = height // cell_size

    # Create the grid
    grid = create_grid(grid_width, grid_height, cell_size)
    grid = place_glider(grid, 2, 10)
    grid = place_glider(grid, 2, 19, flip_x=True)

    # Store the state of the grid
    cell_states = [[cell.is_alive for cell in row] for row in grid]

    # Clock for controlling frame rate
    clock = pygame.time.Clock()

    dragging = False
    drag_start_x = 0
    drag_start_y = 0
    offset_x = 0
    offset_y = 0
    running = True
    paused = True  # Start with the game paused

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused  # Toggle pause

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button (place cells)
                    # Get the mouse position relative to the screen
                    mx, my = pygame.mouse.get_pos()

                    # Adjust the mouse position based on the current offset (due to panning)
                    x, y = (mx - offset_x) // cell_size, (my - offset_y) // cell_size

                    # Ensure the coordinates are within the grid bounds
                    if 0 <= x < grid_width and 0 <= y < grid_height:
                        grid[y][x].toggle_state()  # Toggle the state of the clicked cell
                        cell_states[y][x] = grid[y][x].is_alive  # Update the cell state

                elif event.button == 3:  # Right mouse button (start panning)
                    dragging = True
            
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 3:  # Right mouse button (stop panning)
                    dragging = False

            elif event.type == pygame.MOUSEMOTION:
                if dragging:
                    # Get the mouse movement delta
                    dx, dy = pygame.mouse.get_rel()
                    
                    # Update the offset based on the mouse movement
                    offset_x += dx
                    offset_y += dy
            
            elif (
                event.type == pygame.MOUSEWHEEL
                and pygame.key.get_pressed()[pygame.K_LCTRL]
                or pygame.key.get_pressed()[pygame.K_RCTRL]
            ):
                if event.y > 0:  # Zoom In
                    cell_size = min(cell_size + 5, 100)  # Limit max zoom level
                elif event.y < 0:  # Zoom Out
                    cell_size = max(cell_size - 5, 10)  # Limit min zoom level

                # Recalculate grid dimensions based on the new cell size
                grid_width = width // cell_size
                grid_height = height // cell_size

                # Create a new grid with the updated dimensions
                new_grid = create_grid(grid_width, grid_height, cell_size)

                # Resize the cell_states to match the new grid size
                new_cell_states = [
                    [False for _ in range(grid_width)] for _ in range(grid_height)
                ]

                # Transfer the states from the old grid to the new one, ensuring we don't go out of bounds
                for y in range(min(len(new_grid), len(cell_states))):
                    for x in range(min(len(new_grid[0]), len(cell_states[y]))):
                        new_cell_states[y][x] = cell_states[y][x]

                # Update the cell_states with the new one
                cell_states = new_cell_states

                # Apply the saved states to the new grid
                for y in range(len(new_grid)):
                    for x in range(len(new_grid[0])):
                        new_grid[y][x].is_alive = cell_states[y][x]

                # Set the grid to the newly resized grid
                grid = new_grid

            elif event.type == pygame.VIDEORESIZE:
                # Handle window resizing
                width, height = event.w, event.h
                # Recalculate the number of columns and rows based on new window size
                grid_width = width // cell_size
                grid_height = height // cell_size

                # Create a new grid with the updated dimensions
                new_grid = create_grid(grid_width, grid_height, cell_size)

                # Resize the cell_states to match the new grid size
                new_cell_states = [
                    [False for _ in range(grid_width)] for _ in range(grid_height)
                ]

                # Transfer the states from the old grid to the new one, ensuring we don't go out of bounds
                for y in range(min(len(new_grid), len(cell_states))):
                    for x in range(min(len(new_grid[0]), len(cell_states[y]))):
                        new_cell_states[y][x] = cell_states[y][x]

                # Update the cell_states with the new one
                cell_states = new_cell_states

                # Apply the saved states to the new grid
                for y in range(len(new_grid)):
                    for x in range(len(new_grid[0])):
                        new_grid[y][x].is_alive = cell_states[y][x]

                # Set the grid to the newly resized grid
                grid = new_grid

        # Update the grid only if not paused
        if not paused:
            grid = update_grid(grid)

        # Draw everything
        screen.fill(DEAD_COLOR)  # Clear the screen
        draw_grid(screen, grid, cell_size, offset_x, offset_y)
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

    # Quit Pygame
    pygame.quit()
