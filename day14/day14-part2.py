import re
import sys


# First parameter to program is the input file
with open(sys.argv[1]) as f:
    mem = dict()
    mem_regex = re.compile(r'^mem\[(?P<address>\d+)] = (?P<value>\d+)\s*$')
    for line in f:
        if line[1] == 'a':
            # Set a new mask
            mask = [(bit, value) for bit, value in enumerate(reversed(line.split('=')[1].strip())) if value != '0']
        else:
            # Write something to memory
            data = mem_regex.match(line)
            targets = [int(data['address'])]
            for (bit, value) in mask:
                if value == '1':
                    targets = [address | (1 << bit) for address in targets]
                else:
                    # assert: value == 'X'
                    targets = targets + [address ^ (1 << bit) for address in targets]
            for address in targets:
                mem[address] = int(data['value'])
    print(sum(mem.values()))
