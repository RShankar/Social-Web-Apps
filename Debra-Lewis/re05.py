# Python for Informatics, Chapter 11, example 5 (page 131, section 11.2)
# searches a string for e-mail addresses (string@string)
# Note: \S matches all non-whitespace characters

import re

s = 'Hello from csev@umich.edu to cwen@iupui.edu about the meeting @2PM'
lst = re.findall('\S+@\S+', s)
print lst