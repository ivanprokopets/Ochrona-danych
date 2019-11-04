# -*- coding: utf-8 -*-
"""
Created on 2019

@author: Ivan
"""
# Zaimplementuj algorytm szybkiego potęgowania w artmetyce modularnej. #OK

import sys

x = int(sys.argv[1])
n = int(sys.argv[2])


def qpow(x, n):
    if n == 0:
        return 1
    if n % 2 != 0:
        p = (qpow(x, (n - 1) / 2))
        return x * p * p
    wynik = (qpow(x, n / 2))
    return wynik * wynik


print(qpow(x, n))
