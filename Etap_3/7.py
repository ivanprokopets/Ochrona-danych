import string
import sys, string, crypt
from hmac import compare_digest as compare_hash
from itertools import *
def bruteforce(plik,dlug):
    base = open(plik,'r')
    chars = string.ascii_lowercase
    posiblekey = product(chars, repeat=dlug)
    base=base.readlines()
    for line in base:
        rec = str.split(line, ':')
        rec=rec[1].strip()
        for key in posiblekey:
            sts = ''
            for k in key:
                sts = sts + k
            if compare_hash(crypt.crypt(sts, rec), rec):
                print("Password is found ...", sts)
                break
            else:
                sts = ''
