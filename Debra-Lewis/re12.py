# Python for Informatics, Chapter 11, example 11 (page 137, section 11.5)
# Demonstrating the use of the escape character '\'

import re
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+',x)

print y