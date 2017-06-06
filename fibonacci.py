#! /usr/bin/env python3.5
#! -*- coding: utf-8 -*-

import os

def fibo(nums):
    fibo_nums = [0,1]
    n = 2
    while fibo_nums[n-1]+fibo_nums[n-2] < nums:
        fibo_nums.append(fibo_nums[n-1]+ fibo_nums[n-2])
        n+=1
    return fibo_nums

if __name__ == '__main__':
    print(fibo(1000))
