"""
This program reads a list of directions and prints the "Manhattan distance" to the position obtained by following
each direction in order. Directions involve the behavior of both a ship, which begins at (0, 0), and a waypoint, which
begins 10 units east and 1 unit north of the starting location of the ship.

Directions consist of a capital letter followed by an integer, with the following rules:
- There are only four move directions: North, South, East, and West, each indicated by their initial character
- A cardinal direction indicates a move for the waypoint in the given direction by the given number of units
- L and R indicate respectively a counter-clockwise or clockwise rotation around the current position of the ship
- An F indicates a move in current-facing direction by a given number of times toward the waypoint
- The waypoint moves with the ship whenever the ship moves

Assumptions:
- Left and right rotations may only be executed by 90, 180, or 270 degrees
- No rotations will occur when the waypoint is positioned directly on top of the ship

Notes:
- North and East are represented as positive
- South and West are represented as negative
"""
import sys


# First parameter to program is the input file
with open(sys.argv[1]) as f:
    # Track the position of the ship [E/W, N/S]
    ship_pos = [0, 0]
    # Track the position of the waypoint relative to the ship [E/W, N/S]
    waypoint_pos = [10, 1]
    for line in f:
        line = line.rstrip()
        if line[0] == 'N':
            waypoint_pos[1] += int(line[1:])
        elif line[0] == 'S':
            waypoint_pos[1] -= int(line[1:])
        elif line[0] == 'E':
            waypoint_pos[0] += int(line[1:])
        elif line[0] == 'W':
            waypoint_pos[0] -= int(line[1:])
        elif line[0] == 'F':
            ship_pos[0] += int(line[1:]) * waypoint_pos[0]
            ship_pos[1] += int(line[1:]) * waypoint_pos[1]
        else:
            degrees = int(line[1:])
            if degrees == 180:
                waypoint_pos[0] *= -1
                waypoint_pos[1] *= -1
            elif (line[0] == 'L' and degrees == 90) or (line[0] == 'R' and degrees == 270):
                temp = -1 * waypoint_pos[1]
                waypoint_pos[1] = waypoint_pos[0]
                waypoint_pos[0] = temp
            else:
                temp = -1 * waypoint_pos[0]
                waypoint_pos[0] = waypoint_pos[1]
                waypoint_pos[1] = temp
    print(abs(ship_pos[0]) + abs(ship_pos[1]))
