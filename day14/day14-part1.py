import re
import sys


# First parameter to program is the input file
with open(sys.argv[1]) as f:
    mem = dict()
    mem_regex = re.compile(r'^mem\[(?P<address>\d+)] = (?P<value>\d+)\s*$')
    for line in f:
        if line[1] == 'a':
            # Set a new mask
            mask = [(bit, int(value)) for bit, value in enumerate(reversed(line.split('=')[1].strip())) if value != 'X']
        else:
            # Write something to memory
            data = mem_regex.match(line)
            number = int(data['value'])
            for (bit, value) in mask:
                if value == 0:
                    number &= ~(1 << bit)
                else:
                    # assert: value == 1
                    number |= (1 << bit)
            mem[data['address']] = number
    print(sum(mem.values()))
