"""
This program reads a bus schedule from an input file and prints out the value of the ID of the earliest bus available
(given an earliest possible departure time) multiplied by the number of minutes after the given earliest possible
departure time that bus will arrive.
"""
import re
import sys


# First parameter to program is the input file
with open(sys.argv[1]) as f:
    bus_id_regex = re.compile(r'(?:^|,)(\d+)(?:,|$)')
    earliest_time = int(f.readline())
    final_bus_id = earliest_time * 2
    wait = earliest_time
    for bus_id in (int(bus[1]) for bus in bus_id_regex.finditer(f.readline())):
        new_wait = bus_id - (earliest_time % bus_id)
        if new_wait < wait:
            wait = new_wait
            final_bus_id = bus_id
    print(final_bus_id * wait)
