"""
This program:
- reads in a list of unordered integers from an input file.
- prints the number of ordered permutations of the list such that:
  - at least one value in the set {1, 2, 3} is present in the permutation
  - MAX(list) is present in the permutation
  - for every x in the permutation (with the exception of MAX(list)), at least one element from the list
    {x+1, x+2, x+3} is present in the permutation

Assumptions:
- One value per line in the input file
- Each value is an integer
- There are no duplicate values in the input
- At least one of the values in the set {1, 2, 3} are present in the file
- For every value N present which is greater than 3, at least one value in the set {N-1, N-2, N-3} is also present
"""
import sys


with open(sys.argv[1]) as f:
    nums = {int(line.rstrip()) for line in f}
    counts = dict()
    max_num = max(nums)
    counts[max_num] = 1
    for num in reversed(range(max_num)):
        counts[num] = sum((counts[i] for i in (num + 1, num + 2, num + 3) if i in nums))
    print(counts[0])
