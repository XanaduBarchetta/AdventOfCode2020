import sys


MAPPING = {
    '.': 0,
    '#': 1
}

# First parameter to program is the input file
with open(sys.argv[1]) as f:
    # Initialize cube
    cube = {}
    line = f.readline().rstrip()
    x_start = 0
    x_stop = len(line)
    for x, char in enumerate(line):
        cube[(x, 0, 0)] = MAPPING[char]
    y = 0
    for line in f:
        y += 1
        for x, char in enumerate(line.rstrip()):
            cube[(x, y, 0)] = MAPPING[char]

    # Iterate the cube
    total = 0
    for i in range(1, 7):
        total = 0  # This is only really useful on the last iteration of the loop, but is easier to code this way
        next_cube = {}
        for z in range(0 - i, i + 1):
            for y in range(x_start - i, x_stop + i):
                for x in range(x_start - i, x_stop + i):
                    neighbors = sum(
                        sum(
                            sum(cube.get((xp, yp, zp), 0) for xp in range(x - 1, x + 2))
                            for yp in range(y - 1, y + 2)
                        ) for zp in range(z - 1, z + 2)
                    )
                    is_active = cube.get((x, y, z), 0)
                    neighbors -= is_active
                    if is_active and neighbors not in (2, 3):
                        next_cube[(x, y, z)] = 0
                    elif not is_active and neighbors == 3:
                        next_cube[(x, y, z)] = 1
                        total += 1
                    else:
                        next_cube[(x, y, z)] = is_active
                        total += is_active
        cube = next_cube

    print(total)
