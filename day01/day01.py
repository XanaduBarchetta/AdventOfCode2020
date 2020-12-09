"""
This program prints the product of the first two integers from an input file which sum to a given value.
If no such numbers are found, the program exits silently.
Input file is provided as the first parameter to the script.

Assumptions:
- One value per line
- Each value is an integer
- There are no duplicate values in the input
- The value equal to half of SUM is not present in the input
"""
import sys


SUM = 2020


with open(sys.argv[1]) as f:
    nums = {int(line.rstrip()) for line in f}
    for num in nums:
        if SUM - num in nums:
            print(num * (SUM - num))
            break
