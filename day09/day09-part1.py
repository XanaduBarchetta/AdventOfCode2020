import sys


# First parameter to program is the input file
with open(sys.argv[1]) as f:
    last25 = []
    sums = dict()
    for i in range(0, 25):
        value = int(f.readline())
        for x in last25:
            sums[x].add(x + value)
        last25.append(value)
        sums[value] = set()
    value = int(f.readline())
    while value in set().union(*sums.values()):
        sums.pop(last25.pop(0))
        for x in last25:
            sums[x].add(x + value)
        last25.append(value)
        sums[value] = set()
        value = int(f.readline())
    print(value)
