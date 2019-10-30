# 3. Napisz program przeprowadzający atak brutalnej siły na kryptogram crypto.rc4.
# Został on zaszyfrowany trzyznakowym kluczem 3x ['a'-'z']

from typing import Iterable
from itertools import *
from Crypto.Cipher import ARC4
import sys
import math


def entropy(data: bytes) -> float:
    count = [0] * 256
    dataSize = len(data)
    for b in data:
        count[b] = count[b] + 1
    entropy = 0
    for b in range(256):
        if count[b] / dataSize > 0:
            entropy = entropy + (count[b] / dataSize) * math.log(count[b] / dataSize, 2)
    return -entropy


def codesToStr(codes: Iterable[int]) -> str:
    return ''.join((chr(c) for c in codes))


def bruteforce(cryptogram: bytes, maxKeyLength, keyAlphabet) -> None:
    poprawnaentropija = 7
    # od 5 do 7

    for length in range(1, maxKeyLength + 1):
        possibleKeys = product(keyAlphabet, repeat=length)
        for key in possibleKeys:
            key = codesToStr(key)
            cipher = ARC4.new(key)
            text = cipher.decrypt(cryptogram)

            e = entropy(text)

            if e < poprawnaentropija:
                print("Udało się:" + " " + key)
                print("Text: {}", text)
                sys.exit(0)
        print("nie udało się dla:" + " " + key)


with open('crypto.rc4', 'rb') as file:
    data = file.read()

    keyAlphabet = range(ord('a'), ord('z') + 1)
    bruteforce(data, 3, keyAlphabet)
