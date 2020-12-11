"""
This program reads lines consisting of password policies and an associated password, then prints out the number of
passwords which meet the password policy.

For this program, a password adheres to the policy if it contains no fewer than the minimum and no greater than the
maximum required instances of a given letter.
"""
import re
import sys


VALID_LINE = re.compile(r'^(?P<min_count>\d+)-(?P<max_count>\d+)\s+(?P<letter>[a-z]):\s+(?P<password>[a-z]+)\s*$')


with open(sys.argv[1]) as f:
    valid_count = 0
    for line in f:
        parsed = VALID_LINE.fullmatch(line)
        letter_count = sum((1 for letter in parsed['password'] if letter == parsed['letter']))
        if int(parsed['min_count']) <= letter_count <= int(parsed['max_count']):
            valid_count += 1
    print(valid_count)
