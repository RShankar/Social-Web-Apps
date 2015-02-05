# Python for Informatics, Chapter 11, example 2 (page 130)
# Searches the file for lines that start with the string "From:"
# Note: '^' tells the regex engine to look for a match ONLY at the beginning of the line.

import re

hand = open('mbox-short.txt')

for line in hand:
    line = line.rstrip()
    if re.search('^From:', line) :
        print line