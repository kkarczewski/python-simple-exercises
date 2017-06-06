#! /usr/bin/env python3.5
#! -*- coding: utf-8 -*-

import os
import functools
import math

#Pierwsza wersja - do poprawy
def nww():
    n=1
    while n:
        n+=1
        if n%1==0 and n%2==0 and n%3==0 and n%4==0 and n%5==0 and n%6==0 and n%7==0 and n%8==0 and n%9==0 and n%10==0:
           return n

# Za wiki: Reduction by the greatest common divisor
# nww(a,b) = (x/nwd(x,y))*y
def nww_with_libs():
    return functools.reduce(lambda x,y: y*x//math.gcd(x,y), range(4,44))

if __name__ == '__main__':
    print(nww())
    print(nww_with_libs())
