class Cell:
    def __init__(self, x, y, is_alive=False):
        """
        Initialize a cell.
        :param x: X-coordinate of the cell on the grid.
        :param y: Y-coordinate of the cell on the grid.
        :param is_alive: Boolean indicating whether the cell is alive.
        """
        self.x = x
        self.y = y
        self.is_alive = is_alive

    def toggle_state(self):
        """
        Toggle the cell's state (alive to dead or dead to alive).
        """
        self.is_alive = not self.is_alive