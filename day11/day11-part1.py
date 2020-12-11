"""
This program is essentially a modified Conway's Game of Life with the following rules:
- period character '.' represents no seat
- ell character 'L' represents an empty seat
- hash character '#' represents an occupied seat
- an empty seat with zero adjacent neighbors becomes occupied on the next iteration
- an occupied seat with at least four occupied neighbors becomes empty on the next iteration

- The program prints out the number of occupied seats once the board has stabilized (see assumptions)

Assumptions:
- Each line in the input file is of the same length (the grid is rectangular)
- No wrapping around borders
- The board will eventually stabilize, i.e., there exists some state s such that, for its next state s+1, s == s+1
"""
import sys


def iterate(grid, rows, cols):
    stable = True
    # Deep copy the values
    next_state = [[grid[row][col] for col in range(cols)] for row in range(rows)]
    for row in range(0, rows):
        for col in range(0, cols):
            # Only check seats, never empty spaces
            if grid[row][col] != -1:
                neighbors = 0
                # Check row above (if it exists)
                if row - 1 >= 0:
                    if col - 1 >= 0 and grid[row-1][col-1] == 1:
                        neighbors += 1
                    if col + 1 < cols and grid[row-1][col+1] == 1:
                        neighbors += 1
                    if grid[row-1][col] == 1:
                        neighbors += 1
                # Check row below (if it exists)
                if row + 1 < rows:
                    if col - 1 >= 0 and grid[row+1][col-1] == 1:
                        neighbors += 1
                    if col + 1 < cols and grid[row+1][col+1] == 1:
                        neighbors += 1
                    if grid[row+1][col] == 1:
                        neighbors += 1
                # Check current row
                if col - 1 >= 0 and grid[row][col-1] == 1:
                    neighbors += 1
                if col + 1 < cols and grid[row][col+1] == 1:
                    neighbors += 1
                # Change next state accordingly
                if grid[row][col] == 0 and neighbors == 0:
                    next_state[row][col] = 1
                    stable = False
                elif grid[row][col] == 1 and neighbors >= 4:
                    next_state[row][col] = 0
                    stable = False
                # Else, state was already copied

    return stable, next_state


def main():
    # First parameter to program is the input file
    with open(sys.argv[1]) as f:
        lookup = {
            '.': -1,
            'L': 0,
            '#': 1
        }
        grid = [[lookup[char] for char in line.rstrip()] for line in f]
        rows = len(grid)
        cols = len(grid[0])
        stable = False
        while not stable:
            (stable, grid) = iterate(grid, rows, cols)
        print(sum((sum((1 for seat in row if seat == 1)) for row in grid)))


if __name__ == '__main__':
    main()
