# Conway's Game of Life

Conway’s Game of Life is a cellular automaton devised by mathematician John Horton Conway in 1970. It is a zero-player game where the evolution of a grid of cells is determined by a simple set of rules, leading to fascinating patterns and behaviors.

This Python implementation of the Game of Life allows you to interact with the grid, create custom patterns, and observe how they evolve over time.

---

### How It Works

1. **Grid:** The game is played on a 2D grid where each cell can be either alive (green) or dead (black).
2. **Rules:** 
    - A live cell with fewer than 2 or more than 3 neighbors dies.
    - A dead cell with exactly 3 neighbors becomes alive.
    - All other cells remain unchanged.
3. **Generations:** The game updates the grid based on these rules, producing a new generation.

The simulation continues indefinitely, or until you pause or exit.

---


### Features
- **Interactive Grid:**
    - Left-click on cells to toggle their state (alive or dead).
    - Press SPACE to pause or resume the simulation.
- **Predefined Patterns:**
    - You can create famous patterns like gliders, oscillators, and still     
    - lifes manually or through helper functions.
- **Customizable Settings:**
    - Change the grid size, cell size, and update speed (FPS) in the code.

---

### Patterns
The Game of Life is known for producing fascinating and complex behaviors. Here are a few notable patterns:

#### 1. Glider
A glider is a small pattern that moves diagonally across the grid.

![Glider](https://i.imgur.com/25yY3Bm.png)

#### 2. Still Lifes

These are stable patterns that do not change over generations. Examples:

- **Block**

- **Behive**

![Still Lifes](https://i.imgur.com/V5URI8M.png)


#### 3. Oscillators

These patterns cycle through a set of states and return to their original state after a fixed number of generations.


- **Toad** (period 2):

- **Blinker** (period 2):

![Oscillators](https://i.imgur.com/67Ifta3.png)

#### 4. Spaceships
Patterns that move across the grid.

