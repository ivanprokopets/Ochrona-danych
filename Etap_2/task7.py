from Crypto.Cipher import AES
from typing import Iterable
from itertools import *
import math
from Crypto.Protocol.KDF import PBKDF2


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


def bruteforce(cryptogram: bytes, l, alfabet):
    possibylekey = product(alfabet, alfabet, alfabet)
    for key in possibylekey:
        keystring = codesToStr(key)
        print(keystring)
        key = PBKDF2(keystring, b'abc')
        iv = 16 * "a"
        aes = AES.new(key, AES.MODE_CBC, iv)
        encrypted = aes.decrypt(cryptogram)
        entropija = entropy(encrypted)
        if entropija < 6:
            print("Haslo zostało znalezione: ", keystring)
            exit(0)
