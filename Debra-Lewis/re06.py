# Python for Informatics, Chapter 11, example 6 (page 132, section 11.2)
# Prints out all possible email addresses from a file
# (Anything that is string@string)
import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('\S+@\S+', line)
    if len(x) > 0 :
        print x