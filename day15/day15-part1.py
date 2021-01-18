import sys


# First parameter to program is the input file
with open(sys.argv[1]) as f:
    nums_spoken = 1
    nums = dict()
    for num in f.readline().split(','):
        nums[int(num)] = nums_spoken
        nums_spoken += 1
    # Assume no duplicates in starting nums
    next_num = 0
    while nums_spoken < 2020:
        age = nums.get(next_num, 0)
        nums[next_num] = nums_spoken
        if age:
            age = nums_spoken - age
        next_num = age
        nums_spoken += 1
    print(next_num)
