# -*- coding: utf-8 -*-
"""
Created on 2019

@author: Ivan
"""
# Przy pomocy wywołania bibliotecznej funkcji md5() odtwórz działanie programu md5sum.

import hashlib, sys

plik = sys.argv[1]
m = hashlib.md5(open(plik,'rb').read())
print (m.hexdigest())