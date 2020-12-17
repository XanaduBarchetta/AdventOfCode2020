"""
This program reads a map of trees and prints the number of trees encountered on a (+3, -1) trajectory down the map
with wrapping borders.
"""
import sys


with open(sys.argv[1]) as f:
    x = 3
    trees = 0
    cols = len(f.readline().rstrip())
    for line in f:
        if line[x] == '#':
            trees += 1
        x = (x + 3) % cols
    print(trees)
