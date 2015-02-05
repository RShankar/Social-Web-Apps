# Python for Informatics, Chapter 11, example 7 (page 133, section 11.2)
# Prints all email addresses from a file, ignoring unnecessary characters
# (e.g. the '<' and '>' around some addresses)

import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
    if len(x) > 0:
        print x