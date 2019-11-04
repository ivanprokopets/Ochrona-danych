import sys
import random

text1 = open(sys.argv[1]).read()
text2 = open(sys.argv[2]).read()


def trivial_hash(dane):
    hash = 0
    for znak in dane:
        hash += ord(znak)
    return hash % 999


hash1 = trivial_hash(text1)
hash2 = trivial_hash(text2)

print("haszh t1: " + str(hash1))
print("hasz t2: " + str(hash2))
bialeznaki = {' ', '\n', '\t'}
i = 0
while int(hash1) != int(hash2):
    for znak in text1:
        if not (text1.isspace()):
            text2 = text1
        else:
            text2 = bialeznaki+1
            while (text1 != text2):
                text2 = bialeznaki+1

    hash2 = trivial_hash(text2)
    i += 1
    if (i == 10000):
        print("nie dziala")
        i = 0;

print("po kolizji : ")

print("haszh t1: " + str(hash1))
print("hasz t2: " + str(hash2))
