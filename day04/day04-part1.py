"""
This program reads from an input a list of passports and prints out the number of valid passports, i.e., those
passports with all mandatory fields.

Assumptions:
- No field will occur more than once for a given passport
"""
import sys


with open(sys.argv[1]) as f:
    mandatory_creds = ["ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"]
    current_creds = 0
    valid_passports = 0
    for line in f:
        if line == '\n':
            if current_creds == 7:  # 7 == len(mandatory_creds)
                valid_passports += 1
            current_creds = 0
        else:
            current_creds += sum((1 for field in line.split(' ') if field[:3] in mandatory_creds))
    print(valid_passports)
