import string
import sys


# First parameter to program is the input file
with open(sys.argv[1]) as f:
    answers = []
    all_possible_answers = set(string.ascii_lowercase)
    total = 0
    for line in f:
        if line == '\n':
            total += len(all_possible_answers.intersection(*answers))
            answers = []
        else:
            answers.append(set(line.rstrip()))
    # Sum again in case the file doesn't end in empty line
    total += len(all_possible_answers.intersection(*answers))
    print(total)
