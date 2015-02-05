# Python for Informatics, Chapter 11, example 1 (page 129)
# Searches mbox-short.txt for lines that contain the string "From:"

import re

hand = open('mbox-short.txt')

for line in hand:
    line = line.rstrip()
    if re.search('From:', line) :
        print line