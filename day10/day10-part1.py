"""
This program:
- reads in a list of unordered integers from an input file.
- counts the number (N) of values (x) for which (x+1) appears in the list.
- counts the number (M) of values (y) for which (y+3) appears in the list, but neither (y+1) nor (y+2) appear
- prints the value (N*M)

Assumptions:
- One value per line in the input file
- Each value is an integer
- There are no duplicate values in the input
- At least one of the values in the set {1, 2, 3} are present in the file
- For every value N present which is greater than 3, at least one value in the set {N-1, N-2, N-3} is also present
"""
import sys


with open(sys.argv[1]) as f:
    nums = [int(line.rstrip()) for line in f]
    one_count = 0
    three_count = 0
    if 1 in nums:
        one_count = 1
    elif 2 not in nums:
        three_count = 1
    for num in nums:
        if num + 1 in nums:
            one_count += 1
        elif num + 2 not in nums:
            three_count += 1
    print(one_count * three_count)
