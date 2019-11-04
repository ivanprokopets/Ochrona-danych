# -*- coding: utf-8 -*-
"""
Created on 2019

@author: Ivan
"""
#Zaimplementuj prosty test pierwszości dla liczby (np. sito Erastotenesa, test Fermata).
import sys
import math

from numpy import random
from urllib3.connectionpool import xrange

# FERMAT

def fermat(k, p):
    i = 0

    while i < k:
        a = random.randint(1, p - 1)
        if pow(a, (p - 1), p) == 1:
            i = i + 1
        else:
            return False
    return True


a = int(sys.argv[1])
b = int(sys.argv[2])

if fermat(a, b):
    print("Liczba jest pierwsza\n")
else:
    print("Liczba nie jest pierwsza\n")



