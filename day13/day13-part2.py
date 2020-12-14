"""
This program reads a bus schedule from an input file and prints out the solution to the problem stated here:
https://adventofcode.com/2020/day/13#part2. Description has been omitted for sanity.

Assumptions:
- All bus IDs in the input file are prime integers
"""
import sys


# First parameter to program is the input file
with open(sys.argv[1]) as f:
    _ = int(f.readline())  # No longer relevant
    bus_ids = [(index, int(bus_id)) for index, bus_id in enumerate(f.readline().split(',')) if bus_id != 'x']
    # Begin with the product of all the bus_ids
    factor = bus_ids[0][1]
    value = bus_ids[0][0]
    for remainder, prime in bus_ids[1:]:
        while (value + remainder) % prime != 0:
            value += factor
        factor *= prime
    print(value)
