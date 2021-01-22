import re
import sys

from collections import defaultdict


RULE_REGEX = re.compile(r'^(?P<name>.+): (?P<min1>\d+)-(?P<max1>\d+) or (?P<min2>\d+)-(?P<max2>\d+)\s*$')

# First parameter to program is the input file
with open(sys.argv[1]) as f:
    rules = defaultdict(set)
    rule_names = []
    valid_tickets = []
    valid_values = set()

    # Process rules
    line = f.readline()
    while line != '\n':
        data = RULE_REGEX.match(line)
        rule_names.append(data['name'])
        for value in range(int(data['min1']), int(data['max1']) + 1):
            rules[value].add(data['name'])
            valid_values.add(value)
        for value in range(int(data['min2']), int(data['max2']) + 1):
            rules[value].add(data['name'])
            valid_values.add(value)
        line = f.readline()

    # Build potential rule position dict
    positions = []
    for _ in range(0, 20):
        positions.append(set(name for name in rule_names))

    # Skip unnecessary line
    f.readline()

    my_ticket = [int(x) for x in f.readline().rstrip().split(',')]

    # Skip unnecessary lines
    f.readline()
    f.readline()

    # Process tickets to determine order of rules
    line = f.readline()
    while line != '':
        possible_rules = []
        for value in line.rstrip().split(','):
            value = int(value)
            if value not in valid_values:
                # Discard invalid ticket
                break
            else:
                possible_rules.append(rules[value])
        else:
            # We have a valid ticket. Proceed to reduce possibilities.
            for i in range(0, 20):
                positions[i].intersection_update(possible_rules[i])
        line = f.readline()

    # Reduce possibilities
    found_indices = set()
    while sum(len(item) for item in positions) > 20:
        fixed_rule = ''
        fixed_index = -1
        for i in range(0, 20):
            if i not in found_indices and len(positions[i]) == 1:
                fixed_rule = positions[i].pop()
                positions[i].add(fixed_rule)
                fixed_index = i
                found_indices.add(i)
                break
        for i in range(0, 20):
            if i not in found_indices:
                positions[i].remove(fixed_rule)

    # Get indices of relevant rules
    indices = [index for index, value in enumerate(positions) if value.pop().startswith('departure')]

    total = 1
    for i in indices:
        total *= my_ticket[i]

    print(total)
