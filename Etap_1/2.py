# 2. Porównaj rozkłady statystyczne tekstów w dwóch różnych językach.
# Należy wypisać co najmniej słownik z liczbą wystąpień każdego znaku tekstu.
import re

f = open('angielski.txt')
fpolski = open('polski.txt')
stat = {}
for line in f:
    line = re.sub(r'\s', '', line)
    for znak in line:
        if znak in stat:
            stat[znak] += 1
        else:
            stat[znak] = 0
sorted_x = sorted(stat.items(), key=lambda item: item[1], reverse=True)
print("jezyk angileski\n", sorted_x)
statan = {}
for line in fpolski:
    line = re.sub(r'\s', '', line)
    for znak in line:
        if znak in statan:
            statan[znak] += 1
        else:
            statan[znak] = 0
sorted_y = sorted(statan.items(), key=lambda item: item[1], reverse=True)
print("Jezyk poslki\n", sorted_y)
