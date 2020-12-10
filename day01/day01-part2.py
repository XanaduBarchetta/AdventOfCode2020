"""
This program prints the product of the first three integers from an input file which sum to a given value.
If no such numbers are found, the program exits silently.
Input file is provided as the first parameter to the script.

Assumptions:
- One value per line
- Each value is an integer
- There are no duplicate values in the input
- The value equal to one-third of SUM is not present in the input
"""
import sys


SUM = 2020


with open(sys.argv[1]) as f:
    nums = {int(line.rstrip()) for line in f}
    found = False
    for num in nums:
        nums2 = nums.difference({num})
        for num2 in nums2:
            if SUM - num - num2 in nums2:
                print(num * num2 * (SUM - num - num2))
                found = True
                break
        if found:
            break
