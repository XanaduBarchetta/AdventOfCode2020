"""
This program reads from an input file a list of boarding passes and prints out the seat ID of the one missing seat on
the plane.
"""
import sys
from collections import defaultdict


with open(sys.argv[1]) as f:
    ids = defaultdict(list)
    for line in f:
        row = int(line[:7].replace('F', '0').replace('B', '1'), 2)
        col = int(line[7:].replace('L', '0').replace('R', '1'), 2)
        ids[row].append(col)
    row = sorted([key for key, value in ids.items() if len(value) < 8])[1]
    print(row * 8 + {0, 1, 2, 3, 4, 5, 6, 7}.difference(ids[row]).pop())
