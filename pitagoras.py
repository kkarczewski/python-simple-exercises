#! /usr/bin/env python3.5
#! -*- coding: utf-8 -*-

import os

def pitagoras():
    suma = 1000
    a=1
    while a <= suma / 3:
        a+=1
        b = 1
        while b <= suma / 2:
            b+=1
            c = suma - a - b
            if a**2+b**2 == c**2 and a+b+c == 1000:
                return [a,b,c]

if __name__ == '__main__':
    
    print(pitagoras())
