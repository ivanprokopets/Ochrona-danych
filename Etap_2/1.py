import sys, re, string

numberofchar = 0
stat = {}
file1 = open('tekst.txt', 'r')

for line in file1:
    line = re.sub(r'\s', '', line)
    for znak in line:
        numberofchar += 1
        if znak in stat:
            stat[znak] += 1
        else:
            stat[znak] = 1

for znak in stat:
    print("%s <=> %d " % (znak, stat[znak]))

import math

entropia = 0.0

for znak in stat:
    p = float(stat[znak]) / float(numberofchar)
    entropia = entropia + p * math.log(p, 2.0)
entropia = entropia * -1
print(entropia)
