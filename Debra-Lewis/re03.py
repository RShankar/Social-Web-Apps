# Python for Informatics, Chapter 11, example 2 (section 1, page 130)
# Searches file for lines that start with "F..m" where '.' 
# represents any character
# Note: '.' always matches any character (including whitespace)
import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^F..m:', line):
        print line