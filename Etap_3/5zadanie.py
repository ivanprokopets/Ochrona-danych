# -*- coding: utf-8 -*-
"""
Created on 2019

@author: Ivan
"""

# Przy pomocy wywołania bibliotecznej funkcji md5()
# odtwórz działanie polecenia md5sum -c, czyli kontrole spójności plików.

import hashlib, sys, string, os

def md5sum(plikName, plikChecksum):
    plik = open(plikName,'rb')
    m = hashlib.md5(plik.read())
    hexdigest = m.hexdigest()
    if os.path.getsize(sys.argv[2]) == 0:
        plikChecksum.write("%s  %s" % (hexdigest, plikName))
    return hexdigest


def md5sumc(plikChecksum):
    for line in plikChecksum.readlines():
        rec = str.split(line, '  ')
        if rec[0] == md5sum(rec[1], plikChecksum):
            return rec[1] + ": OK"
        else:
            return rec[1] + ": FALSE"

plikChecksum = open(sys.argv[2], 'r')
if sys.argv[1] == "-c":
    print(md5sumc(plikChecksum))
else:
    plikChecksum = open(sys.argv[2], 'w')
    print(md5sum(sys.argv[1], plikChecksum))