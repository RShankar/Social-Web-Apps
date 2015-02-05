# Python for Informatics, Chapter 11, example 10 (page 131, section 11.3)
# Extracting revision numbers from a document

import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^Details:.*rev=([0-9.]+)', line)
    if len(x) > 0:
        print x