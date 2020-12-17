"""
This program reads from an input a list of passports and prints out the number of valid passports, i.e., those
passports with all mandatory fields and valid data for those fields.

Assumptions:
- No field will occur more than once for a given passport
- All valid heights are also integers
"""
import re
import sys


with open(sys.argv[1]) as f:
    valid_field = re.compile(r'^(?:'
                             r'byr:(?:19[2-9]\d|200[0-2])|'
                             r'iyr:20(?:1\d|20)|'
                             r'eyr:20(?:2\d|30)|'
                             r'hgt:(?:1(?:[5-8]\d|9[0-3])cm|(?:59|6\d|7[0-6])in)|'
                             r'hcl:#[0-9a-f]{6}|'
                             r'ecl:(?:amb|blu|brn|gr[yn]|hzl|oth)|'
                             r'pid:\d{9}'
                             r')$')
    current_creds = 0
    valid_passports = 0
    for line in f:
        if line == '\n':
            if current_creds == 7:  # 7 == number of mandatory fields
                valid_passports += 1
            current_creds = 0
        else:
            current_creds += sum((1 for field in line.split(' ') if valid_field.match(field)))
    print(valid_passports)
