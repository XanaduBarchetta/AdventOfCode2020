"""
This program reads a map of trees and prints the product of the number of trees encountered across multiple
trajectories.
"""
import sys


with open(sys.argv[1]) as f:
    totals = {
        1: [1, 0],
        3: [3, 0],
        5: [5, 0],
        7: [7, 0]
    }
    other_total = [1, 0]  # track the (+1, +2) trajectory
    even_index = False  # True if we are on an even index for the (+1, +2) trajectory
    cols = len(f.readline().rstrip())
    for line in f:
        for key in totals.keys():
            if line[totals[key][0]] == '#':
                totals[key][1] += 1
            totals[key][0] = (totals[key][0] + key) % cols
        if even_index:
            if line[other_total[0]] == '#':
                other_total[1] += 1
            other_total[0] = (other_total[0] + 1) % cols
        even_index = ~even_index
    total = 1
    for value in totals.values():
        total *= value[1]
    print(total * other_total[1])
