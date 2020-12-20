"""
This program reads from an input file a list of passports and prints out the number of valid passports, i.e., those
passports with all mandatory fields.

Assumptions:
- No field will occur more than once for a given passport
"""
import sys


with open(sys.argv[1]) as f:
    highest_id = 0
    for line in f:
        row = int(line[:7].replace('F', '0').replace('B', '1'), 2)
        col = int(line[-3:].replace('L', '0').replace('R', '1'), 2)
        highest_id = max(highest_id, row * 8 + col)
    print(highest_id)
