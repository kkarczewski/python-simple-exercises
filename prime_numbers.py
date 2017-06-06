#! /usr/bin/env python3.5
#! -*- coding: utf-8 -*-

import os, math

def is_prime(num):
    if num % 2 == 0 and num > 2:
        return False
    return all(num % one for one in range(3, int(math.sqrt(num)) + 1, 2))
    
if __name__ == '__main__':
    prime_numbers = list()
    for one in range(2, 10000):
        if is_prime(one):
            prime_numbers.append(one)
    print(prime_numbers)
    print("Ilość liczb pierwszych:", len(prime_numbers))
