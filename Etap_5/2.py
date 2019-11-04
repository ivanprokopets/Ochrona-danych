# -*- coding: utf-8 -*-
"""
Created on 2019

@author: Ivan
"""
#Napisz funkcje odwrotną, czyli przekształcającą wektor liczb w tekst.

import sys


def numbers_to_text(numbers):
    text = ''
    for x in numbers:
        text += chr(x)

    return text


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        numbers = f.read()
        f.close()

    numbers = numbers.split(' ')
    if '\n' in numbers:
        numbers.remove('\n')
    numbers = [int(n) for n in numbers]
    print(numbers_to_text(numbers))