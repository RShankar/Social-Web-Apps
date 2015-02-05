# Exercise 11.2
import re
fname = raw_input('Enter file:')
hand = open(fname)
nums = list()
for line in hand:
    line = line.rstrip()
    x = re.findall('New Revision: ([0-9]+)', line)
    if len(x) == 1 :
        val = float(x[0])
        nums.append(val)
print sum(nums)/len(nums)

