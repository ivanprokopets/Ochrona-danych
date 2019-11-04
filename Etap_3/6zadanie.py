# -*- coding: utf-8 -*-
"""
Created on 2019

@author: Ivan
"""

# Korzystając z polecania time sprawdź wydajność dowolnej implementacji algorytmu łamania haseł
# metodą brutalnej siły i oszacuj czas maksymalny czas potrzebny do złamania haseł różnej
# długości i składający się z małych liter i dużych liter.

import string, crypt
from datetime import time
from hmac import compare_digest as compare_hash
from itertools import *
import time

import datetime

start = datetime.datetime.now()
print(start)


def bruteforce(passwd, dlug):
    chars = string.ascii_letters
    posiblekey = product(chars, repeat=dlug)
    for key in posiblekey:
        sts = ''
        for k in key:
            sts = sts + k
        if compare_hash(crypt.crypt(sts, passwd), passwd):
            print("haslo zlamane", sts)
            break
        else:
            sts = ''


bruteforce(crypt.crypt("Abc"), 3)
duration = datetime.datetime.now() - start
print(duration)
# print("wynik", bruteforce/time.localtime().tm_sec)
