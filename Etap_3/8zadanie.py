# -*- coding: utf-8 -*-
"""
Created on 2019

@author: Ivan
"""

# Przygotuj dwa dokumenty, których funkcje skrótu trivial_hash() bedą identyczne, a treść różna.
# Wykorzystaj paradoks urodzinowy.

# -*- coding: utf-8 -*-
import sys


def trivial_hash(data):
    hash = 0
    for char in data:
        hash += ord(char)
    return hash % 999

with open(sys.argv[1], 'r') as f:
    file1 = f.read()
    f.close()
with open(sys.argv[2], 'r') as f:
    file2 = f.read()
    f.close()
hash1 = trivial_hash(file1)
hash2 = trivial_hash(file2)

print(hash1, hash2)
