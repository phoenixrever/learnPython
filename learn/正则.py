# coding: utf-8

import re

# pat = re.compile("AA")
# r = pat.search("AAA")

m = re.search("[sa]", "sasds")
n = re.findall("a", "sdasdq")
print(n)

print(re.sub("a", "A", r"abcd", 1))  # replace a with A r 不转义
