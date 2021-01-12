import sys

# First parameter to program is the input file
with open(sys.argv[1]) as f:
    accumulator = 0
    instructions = []
    for line in f:
        instructions.append(line.rstrip())
    visited = set()  # Track which lines of code we've visited
    i = 0  # Current line of code
    while i not in visited:
        visited.add(i)
        if instructions[i][:3] == 'nop':
            i += 1
        elif instructions[i][:3] == 'acc':
            accumulator += int(instructions[i][4:])
            i += 1
        else:
            # assert instructions[i][:3] == 'jmp'
            i += int(instructions[i][4:])
    print(accumulator)
