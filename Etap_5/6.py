# -*- coding: utf-8 -*-
"""
Created on 2019

@author: Ivan
"""
# Napisz funkcję wykorzystającą algorytm Euklidesa do obliczenia liczby odwrotnej modulo. #OK
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


def licz(a, b):
    if wzgled(a, b):
        k = 1
        while (a * k) % b != 1:
            k += 1
        return k
    else:
        return False


def main():
    a = int(sys.argv[1])
    b = int(sys.argv[2])

    if licz(a, b) != 0:
        print(licz(a, b))
    else:
        print("Brak")


if __name__ == "__main__":
    main()
