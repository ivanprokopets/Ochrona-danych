# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 21:56:57 2019

@author: Dom
"""

import sys, re, string, math
import operator
stat = {}
edge = float(256)/ math.log(52,2)
entropy = 0.0
entropy = edge/8
print ("Password should have more than " + str(int(entropy)) + " characters.")
print (entropy )
