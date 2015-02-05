# Python for Informatics, Chapter 11, example 9 (page 134, section 11.3)
# Same idea as example 8, but only prints out the numbers from the matched strings

import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^X\S*: ([0-9.]+)',line)
    if len(x) > 0:
        print x