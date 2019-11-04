# -*- coding: utf-8 -*-
"""
Created on 2019

@author: Ivan
"""
# Napisz program korzystający z PyCrypto do szyfrowania plików. Zaproponuj metodę ochrony klucza prywatnego.

from Crypto.PublicKey import RSA
import sys

rsa_keys = RSA.generate(1024)
# Wydzielenie klucza publicznego
pub_key = rsa_keys.publickey()

with open(sys.argv[1], 'rb') as f:
    file_content = f.read()
    f.close()

#print (file_content)
text = file_content[:150]
print(text)
# Zaszyfrowanie przy pomocy klucza publicznego
encrypted = pub_key.encrypt(text, "some randomness")
print(encrypted)
# Odszyfrowanie kluczem prywatnym
print(rsa_keys.decrypt(encrypted))
