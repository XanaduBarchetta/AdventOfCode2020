import re
import sys

from collections import defaultdict


BAG_REGEX = re.compile(r'([a-z]+ [a-z]+) bag')
MY_BAG = "shiny gold"

# First parameter to program is the input file
with open(sys.argv[1]) as f:
    # Build the rules
    rules = defaultdict(list)
    for line in f:
        bags = BAG_REGEX.findall(line)
        # Ignore bags which can contain no other bags
        if bags[1] != "no other":
            for bag in bags[1:]:
                rules[bag].append(bags[0])

    # Find the different possibilities
    parents = set()
    queue = rules[MY_BAG]
    while len(queue) > 0:
        bag = queue.pop(0)
        if bag not in parents:
            parents.add(bag)
            queue.extend(rules[bag])
    print(len(parents))
