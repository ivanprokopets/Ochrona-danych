# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 22:15:12 2019

@author: Dom
"""

import sys, re, string
import math
from Crypto.Cipher import ARC4


def entropia(data: bytes) -> float:
    count = [0] * 256
    dataSize = len(data)
    for b in data:
        count[b] = count[b] + 1
    entropy = 0
    for b in range(256):
        if count[b] / dataSize > 0:
            entropy = entropy + (count[b] / dataSize) * math.log(count[b] / dataSize, 2)
    return -entropy

cipher = ARC4.new("zzz")
text = cipher.encrypt('To jest test to szyfrowania zoabczymy jak to dziala')

for first in range(0,26):
    for second in range (0,26):
        for third in range(0,26):
            key = chr(ord('a')+first)+chr(ord('a')+second)+chr(ord('a')+third)
            cipher = ARC4.new(key)
            dec = cipher.decrypt(text)
            if (entropia(dec)) < 4.5:
                print (text)
            print (key)
    print (entropia(text))
    print (dec)
print (entropia(dec))