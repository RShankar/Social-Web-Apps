# Python for Informatics, Chapter 11, example 4 (page 131, section 11.1)
# Searches for Strings that start with "From:" and are followed by one 
# or more characters followed by an @ symbol
# Example: 
# From: stephen.marquard@uct.ac.za
#   (matches "From: stephen.marquard")
# Note that the + and * symbols are both greedy, and will also match:
# From: stephen.marquard@uct.ac.za, csev@umic.edu, and cwen@iupui.edu
#   (matches "From: stephen.marquard@uct.ac.za, csev@umic.edu, and cwen")
# '+' expands the previous symbol to match 1 or more times 
# (so '.+' matches any characters 1 or more times)

import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:.+@', line) :
        print line