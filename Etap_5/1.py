# -*- coding: utf-8 -*-
"""
Created on 2019

@author: Ivan
"""
# Napisz funkcje, która będzie przekształcać tekst w wektor liczb o określonej długości. Określ ilość znaków, którą chcesz kodować jednocześnie.


import sys


def text_to_numbers(text):
    numbers = []
    for znak in text:
        numbers.append(ord(znak))
    return numbers


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        text = f.read()
        f.close()
    numbers = text_to_numbers(text)

    for num in numbers:
        sys.stdout.write("%d \n" % (num))
