# Python for Informatics, Chapter 11, example 8 (page 134, section 11.3)
# Prints all lines that start with "X-", are followed by 0 or more characters,
#  followed by a ": " and then followed by one or more characters that are either digits
#  or a "."
# Example: 
#    X-blah: 12.999

import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^X\S*: [0-9.]+',line) :
        print line