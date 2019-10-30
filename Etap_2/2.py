import sys, re, string
from pip._vendor.distlib.compat import raw_input
text = "Motor vehicle manufacturers distribute and ensure the repair and maintenance of their products through authorised dealer and repairer networks. The bundles of similar vertical agreements which make up these networks may require assessment pursuant to Article 81 of the Treaty. Block exemption regulations create safe harbours for categories of agreements that are caught by the prohibition in Article 81(1), relieving the contracting parties from the need to analyse whether those agreements can benefit from the exception provided for in Article 81(3). Block exemptions thus contribute to legal certainty and to the coherent application of EU competition rules across the EU. Agreements not covered by a block exemption are not presumed to be illegal, butinstead have to be assessed individually. "

numberofchar = len(text)

from Crypto.Cipher import ARC4

key = raw_input("podaj klucz")
cipher = ARC4.new(key)
encrypted = cipher.encrypt(text)

numberofchar2 = len(encrypted)

stat = {}
stat2 = {}

line = text
# line = re.sub(r'\s', '', line)
for znak in line:

    if znak in stat:
        stat[znak] += 1
    else:
        stat[znak] = 1

line2 = encrypted
# line2 = re.sub(r'\s', '', line2)
for znak2 in line2:

    if znak2 in stat2:
        stat2[znak2] += 1
    else:
        stat2[znak2] = 1

import math

entropia = 0.0

for znak in stat:
    p = float(stat[znak]) / float(numberofchar)
    entropia += p * math.log(p, 2.0)
entropia *= -1
print("entropia niezaszyfr")
print(entropia)

entropia2 = 0
for znak2 in stat2:
    p2 = float(stat2[znak2]) / float(numberofchar2)
    entropia2 += p2 * math.log(p2, 2.0)
entropia2 *= -1
print("entropia zaszyfr")
print(entropia2)
