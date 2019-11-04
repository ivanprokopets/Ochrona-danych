# -*- coding: utf-8 -*-
"""
Created on 2019

@author: Ivan
"""
# Napisz funkcję wykorzystającą algorytm Euklidesa do sprawdzenia czy liczby są względnie pierwsze. #OK


import sys


def nwd(a, b):
    while b != 0:
        b, a = a % b, b
    return a


def wzgled(a, b):
    if nwd(a, b) == 1:
        return True
    else:
        return False


def main():
    a = int(sys.argv[1])
    b = int(sys.argv[2])

    if wzgled(a, b) == 1:
        print("Liczby {} i {} sa wzglednie pierwsze".format(a, b))
    else:
        print("Liczby {} i {} nie sa wzglednie pierwsze".format(a, b))


if __name__ == "__main__":
    main()
