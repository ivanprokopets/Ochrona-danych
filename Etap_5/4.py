# -*- coding: utf-8 -*-
"""
Created on 2019

@author: Ivan
"""
# Zaimplementuj algorytm Euklidesa do sprawdzenia największego wspólnego dzielnika.

import sys


def nwd(a, b):
    while a != b:
        if a < b:
            b = b - a
        else:
            a = a - b
    return a


def nwd_2(a, b):
    while b != 0:
        b, a = a % b, b
    return a


if __name__ == "__main__":
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print(nwd(a, b))
    print(nwd_2(a, b))

# --------------------
