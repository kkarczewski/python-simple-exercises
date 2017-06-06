#! /usr/bin/env python3.5
#! -*- coding: utf-8 -*-

import os

def is_special(nums):
    for num in nums:
        if (num%3 == 0 and num%5 != 0):
            print('FIZZ')
        elif (num%3!=0 and num%5==0):
            print('BUZZ')
        elif (num%3 == 0 and num%5 == 0):
            print('FIZZBUZZ')
        else:
            print(num)

if __name__ == '__main__':
    n = input("Input n\n")
    numbers = list(i for i in range(1,int(n)+1))
    is_special(numbers)
    
