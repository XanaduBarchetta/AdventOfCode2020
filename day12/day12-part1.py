"""
This program reads a list of directions and prints the "Manhattan distance" to the position obtained by following
each direction in order.

Directions consist of a capital letter followed by an integer, with the following rules:
- Initial-facing direction is East
- There are only four move directions: North, South, East, and West, each indicated by their initial character
- A cardinal direction indicates a move in the given direction by the given number of units
- L and R indicate respectively a left or right rotation (and thus change to current-facing direct) as viewed from the
  helm by the given number of degrees
- An F indicates a move in current-facing direction by the given number of units

Assumptions:
- Left and right turns may only be executed by 90, 180, or 270 degrees
"""
import sys


# First parameter to program is the input file
with open(sys.argv[1]) as f:
    totals = {
        'E': 0,
        'W': 0,
        'N': 0,
        'S': 0
    }
    # Keep track of the current direction at all times
    curr_dir = 'E'
    # This dict maps where a given turn will cause us to face from a given direction
    turn_dir = {
        'E': {
            'L90': 'N',
            'L180': 'W',
            'L270': 'S',
            'R90': 'S',
            'R180': 'W',
            'R270': 'N',
        },
        'W': {
            'R90': 'N',
            'R180': 'E',
            'R270': 'S',
            'L90': 'S',
            'L180': 'E',
            'L270': 'N',
        },
        'N': {
            'L90': 'W',
            'L180': 'S',
            'L270': 'E',
            'R90': 'E',
            'R180': 'S',
            'R270': 'W',
        },
        'S': {
            'R90': 'W',
            'R180': 'N',
            'R270': 'E',
            'L90': 'E',
            'L180': 'N',
            'L270': 'W',
        }
    }
    for line in f:
        line = line.rstrip()
        if line[0] == 'R' or line[0] == 'L':
            # Turn to face a new direction
            curr_dir = turn_dir[curr_dir][line]
        elif line[0] == 'F':
            # Move forward in the current-facing direction
            totals[curr_dir] += int(line[1:])
        else:
            # Move in the given direction
            totals[line[0]] += int(line[1:])
    print(abs(totals['E'] - totals['W']) + abs(totals['N'] - totals['S']))
