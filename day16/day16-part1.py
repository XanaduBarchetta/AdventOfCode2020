import re
import sys


RULE_REGEX = re.compile(r'^(?P<name>.+): (?P<min1>\d+)-(?P<max1>\d+) or (?P<min2>\d+)-(?P<max2>\d+)\s*$')

# First parameter to program is the input file
with open(sys.argv[1]) as f:
    error_rate = 0
    valid_values = set()

    # Process rules
    line = f.readline()
    while line != '\n':
        data = RULE_REGEX.match(line)
        for value in range(int(data['min1']), int(data['max1']) + 1):
            valid_values.add(value)
        for value in range(int(data['min2']), int(data['max2']) + 1):
            valid_values.add(value)
        line = f.readline()

    # Skip unnecessary lines for Part 1
    f.readline()
    f.readline()
    f.readline()
    f.readline()

    # Check for invalid tickets
    for line in f:
        for value in line.split(','):
            value = int(value)
            if value not in valid_values:
                error_rate += value
    print(error_rate)
