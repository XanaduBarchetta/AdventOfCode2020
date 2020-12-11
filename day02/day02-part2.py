"""
This program reads lines consisting of password policies and an associated password, then prints out the number of
passwords which meet the password policy.

For this program, a password adheres to a policy when exactly one of the two provided 1-indexed indexes match the
provided letter in the provided password.
"""
import re
import sys


VALID_LINE = re.compile(r'^(?P<index1>\d+)-(?P<index2>\d+)\s+(?P<letter>[a-z]):\s+(?P<password>[a-z]+)\s*$')


with open(sys.argv[1]) as f:
    valid_count = 0
    for line in f:
        parsed = VALID_LINE.fullmatch(line)
        if (
            parsed['password'][int(parsed['index1']) - 1] == parsed['letter']
        ) != (
            parsed['password'][int(parsed['index2']) - 1] == parsed['letter']
        ):
            valid_count += 1
    print(valid_count)
