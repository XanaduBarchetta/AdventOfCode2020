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

    # Find the target value
    target_value = int(f.readline())
    while target_value in set().union(*sums.values()):
        sums.pop(last25.pop(0))
        for x in last25:
            sums[x].add(x + target_value)
        last25.append(target_value)
        sums[target_value] = set()
        target_value = int(f.readline())

    # Re-process the input to find the required contiguous values
    f.seek(0, 0)
    total = 0
    nums = []
    while total != target_value:
        nums.append(int(f.readline()))
        total += nums[-1]
        while total > target_value:
            total -= nums.pop(0)
    print(min(nums) + max(nums))
