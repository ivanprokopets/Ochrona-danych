# -*- coding: utf-8 -*-
"""
Created on 2019

@author: Ivan
"""
#Zaimplementuj prosty test pierwszości dla liczby (np. sito Erastotenesa, test Fermata).
#SITO OK
import sys
import math

from numpy import random
from urllib3.connectionpool import xrange


def sieve_of_erastotenes(limit):
    output = []
    a = [True] * limit
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            output.append(i)
            for n in xrange(i * i, limit, i):
                a[n] = False
    return output


if __name__ == "__main__":
    print(sieve_of_erastotenes(int(sys.argv[1])))


