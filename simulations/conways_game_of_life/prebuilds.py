def place_glider(grid, x, y, flip_x=False, flip_y=False):
    """
    Places a glider pattern on the grid.
    :param grid: The 2D grid of Cell objects.
    :param x: The starting x-coordinate for the glider.
    :param y: The starting y-coordinate for the glider.
    """
    pattern = [
        (0, 1, 0),
        (0, 0, 1),
        (1, 1, 1),
    ]

    return place_pattern(grid, pattern, x, y, flip_x, flip_y)


def place_blinker(grid, x, y, flip_x=False, flip_y=False):
    """
    Places a blinker pattern on the grid.
    :param grid: The 2D grid of Cell objects.
    :param x: The starting x-coordinate for the blinker.
    :param y: The starting y-coordinate for the blinker.
    """
    pattern = [
        (0, 1),
        (0, 1),
        (0, 1),
    ]

    return place_pattern(grid, pattern, x, y, flip_x, flip_y)


def place_toad(grid, x, y):
    """
    Places a toad pattern on the grid.
    :param grid: The 2D grid of Cell objects.
    :param x: The starting x-coordinate for the toad.
    :param y: The starting y-coordinate for the toad.
    """
    pattern = [
        (0, 1, 1, 1),
        (1, 1, 1, 0),
    ]

    return place_pattern(grid, pattern, x, y)


def place_heavy_weight_spaceship_pattern(grid, x, y, flip_x=False, flip_y=False):
    pattern = [
        (0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0),
        (0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0),
        (0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0),
        (0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0),
        (0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0),
        (0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1),
        (0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0),
        (0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1),
        (0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0),
    ]

    return place_pattern(grid, pattern, x, y, flip_x, flip_y)


def place_pattern(grid, pattern, x, y, flip_x=False, flip_y=False):
    """
    Places a custom pattern on the grid based on the pattern list.
    :param grid: The 2D grid of Cell objects.
    :param pattern: A list of tuples representing the pattern's relative coordinates.
    :param x: The starting x-coordinate for the pattern.
    :param y: The starting y-coordinate for the pattern.
    :param flip_x: If True, the pattern will be flipped horizontally.
    :param flip_y: If True, the pattern will be flipped vertically.
    """
    # If flip_x is True, reverse each row in the pattern
    if flip_x:
        pattern = [row[::-1] for row in pattern]

    # If flip_y is True, reverse the entire pattern vertically
    if flip_y:
        pattern = pattern[::-1]

    # Place the pattern on the grid
    for i in range(len(pattern)):
        for j in range(len(pattern[i])):
            if pattern[i][j] == 1:
                grid[x + i][y + j].is_alive = True

    return grid
