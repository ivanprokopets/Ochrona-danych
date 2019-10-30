# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 19:57:00 2019

@author: Dom
"""

from Crypto.Cipher import AES
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

key = "aaaabbbbccccdddd"
cipher = AES.new(key, AES.MODE_ECB)
with open("demo24.bmp", "rb") as f:
    clear = f.read()
#ciphertext = cipher.encrypt(clear)
len(clear)
a=len(clear) % 16
clear_trimmed = clear[64:-a]
len(clear_trimmed)
len(clear_trimmed) % 16
ciphertext = cipher.encrypt(clear_trimmed)
ciphertext = clear[0:64] + ciphertext + clear[-a:]
e = entropy(ciphertext)
print("Result  ECB:", e)
with open("demo24_ecb.bmp", "wb") as f:
    f.write(ciphertext)
    
    
    
iv = "0000111122223333"
cipher1 = AES.new(key, AES.MODE_CBC, iv)
with open("demo24.bmp", "rb") as fa:
    clear1 = fa.read()
len(clear1)
b=len(clear1) % 16
clear_trimmed1 = clear1[64:-b]
len(clear_trimmed1)
len(clear_trimmed1) % 16
ciphertext1 = cipher1.encrypt(clear_trimmed1)
ciphertext1 = clear1[0:64] + ciphertext1 + clear1[-b:]
w = entropy(ciphertext1)
print("Result  CBC:", w)
with open("demo24_cbc.bmp", "wb") as fa:
  fa.write(ciphertext1)
