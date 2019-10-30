from Crypto.Cipher import DES,AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
import sys
password = "VaniaSuper10"
iv = get_random_bytes(8)
key = PBKDF2(password, iv, 16, 1000, None)
print("algorytm tworzenia klucza na podstawie hasła podawanego przez człowieka\n")
print("klucz na podstawie hasla:",key)