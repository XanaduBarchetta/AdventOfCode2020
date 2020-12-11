"""
This program is essentially a modified Conway's Game of Life with the following rules:
- period character '.' represents no seat
- ell character 'L' represents an empty seat
- hash character '#' represents an occupied seat
- a "line of sight" refers to a vector in one of eight directions looking out from a given point: up, down, left, right,
  and the four diagonals at 45 degree angles between those four directions
- a "neighbor" is the first seat (occupied or empty) in a line of sight starting from a given point
- an empty seat with zero adjacent occupied neighbors becomes occupied on the next iteration
- an occupied seat with at least five occupied neighbors becomes empty on the next iteration

- The program prints out the number of occupied seats once the board has stabilized (see assumptions)

Assumptions:
- Each line in the input file is of the same length (the grid is rectangular)
- No wrapping around borders
- The board will eventually stabilize, i.e., there exists some state s such that, for its next state s+1, s == s+1
"""
import sys


def get_next_neighbor(grid, row, col, east_west, north_south, rows, cols):
    """
    Searches a grid in a given direction from a given starting point and returns the first neighbor.

    :param grid:
    :param row: row coordinate of starting point
    :param col: col coordinate of starting point
    :param east_west: 1 if east, -1 if west, 0 if neither (true north/south)
    :param north_south: 1 if south, -1 if north, 0 if neither (true east/west)
    :param rows: maximum number of rows in the grid
    :param cols: maximum number of columns in the grid
    :return: 1 if the neighbor in the given direction is occupied, 0 otherwise
    """
    row += north_south
    col += east_west
    while 0 <= row < rows and 0 <= col < cols:
        if grid[row][col] == 0:
            return 0
        elif grid[row][col] == 1:
            return 1
        row += north_south
        col += east_west
    return 0


def iterate(grid, rows, cols):
    stable = True
    # Deep copy the values
    next_state = [[grid[row][col] for col in range(cols)] for row in range(rows)]
    for row in range(0, rows):
        for col in range(0, cols):
            # Only check seats, never empty spaces
            if grid[row][col] != -1:
                neighbors = sum((
                    get_next_neighbor(grid, row, col, ew_dir, ns_dir, rows, cols) for ew_dir, ns_dir in [
                        (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
                    ]
                ))
                # Change next state accordingly
                if grid[row][col] == 0 and neighbors == 0:
                    next_state[row][col] = 1
                    stable = False
                elif grid[row][col] == 1 and neighbors >= 5:
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
