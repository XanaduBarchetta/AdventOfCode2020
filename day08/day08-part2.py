import sys

# First parameter to program is the input file
with open(sys.argv[1]) as f:
    accumulator = 0
    original_instructions = []
    changed_instructions = set()
    for line in f:
        original_instructions.append(line.rstrip())

    visited = set()  # Track which lines of code we've visited
    possible_changes = set()  # Track which lines of code could be changed

    # Execute a first pass to see which lines of code could possibly be changed
    i = 0  # Current line of code
    while i not in visited and i < len(original_instructions):
        visited.add(i)
        if original_instructions[i][:3] == 'nop':
            possible_changes.add(i)
            i += 1
        elif original_instructions[i][:3] == 'acc':
            accumulator += int(original_instructions[i][4:])
            i += 1
        else:
            # assert instructions[i][:3] == 'jmp'
            possible_changes.add(i)
            i += int(original_instructions[i][4:])

    while i < len(original_instructions):
        accumulator = 0
        # Change one instruction
        instructions = original_instructions[:]
        i = possible_changes.pop()
        if instructions[i][:3] == 'jmp':
            instructions[i] = 'nop'
        else:
            # assert instructions[i][:3] == 'nop'
            instructions[i] = 'jmp' + instructions[i][3:]

        visited = set()  # Track which lines of code we've visited
        i = 0  # Current line of code
        while i not in visited and i < len(instructions):
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
