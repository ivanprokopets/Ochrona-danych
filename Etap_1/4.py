import re

tekst = "alaa"
stat = {}
counter = 0.0
for line in tekst.splitlines():
    line = re.sub(r'\s', '', line)
    for znak in line:
        counter = counter + 1
        if znak in stat:
            stat[znak] += 1
        else:
            stat[znak] = 1

for znak in stat:
    print("%s <=> %f" % (znak, (stat[znak] / counter) * 100) + "%")
