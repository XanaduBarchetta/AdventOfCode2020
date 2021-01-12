import re
import sys

from collections import defaultdict


BAG_REGEX = re.compile(r'((?:^|\d )[a-z]+ [a-z]+) bag')
MY_BAG = "shiny gold"

# First parameter to program is the input file
with open(sys.argv[1]) as f:
    # Build the rules
    rules = defaultdict(list)
    for line in f:
        bags = BAG_REGEX.findall(line)
        # We automatically ignore "no other" by construction of the regex
        rules[bags[0]].extend([(int(bag[0]), bag[2:]) for bag in bags[1:]])

    # Traverse the bags
    total = 0
    queue = rules[MY_BAG]
    while len(queue) > 0:
        bag = queue.pop(0)
        total += bag[0]
        queue.extend([(bag[0]*rule[0], rule[1]) for rule in rules[bag[1]]])
    print(total)
