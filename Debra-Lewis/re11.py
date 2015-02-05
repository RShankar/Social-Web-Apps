# Python for Informatics, Chapter 11, example 11 (page 136, section 11.3)
# Printing out the hour of day from "From:" lines

import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^From .* ([0-9][0-9]):', line)
    if len(x) > 0:
        print x