import sys


# First parameter to program is the input file
with open(sys.argv[1]) as f:
    answers = set()
    total = 0
    for line in f:
        if line == '\n':
            total += len(answers)
            answers = set()
        else:
            answers = answers.union(set(line.rstrip()))
    # Sum again in case the file doesn't end in empty line
    total += len(answers)
    print(total)
