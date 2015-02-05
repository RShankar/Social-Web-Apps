"""
Exercise 11.1: Write a simple program to simulate the operation of the 
grep command on Unix. Ask the user to enter a regular expression and 
count the number of lines that matched the regular expression.
"""

import re

fname = raw_input('Enter file name: ')
hand = open(fname)

regex = raw_input('Enter a regular expression: ')

val = 0

for line in hand:
    line = line.rstrip()
    x = re.findall(regex, line)
    if len(x) == 1 :
        val = val + 1
        
print fname + " had " + str(val) + " lines that matched " + regex