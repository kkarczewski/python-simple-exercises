#! /usr/bin/env python3.5
#! -*- coding: utf-8 -*-

import os

def is_palindrome(str):
    if str == None or str=='':
        raise Exception('Empty string')
    elif str == str[::-1]:
        print(str, 'is palindrome')
    else:
        print(str, 'is not palindrome')

if __name__ == '__main__':
    input_from_prompt = input("Podaj ciąg znaków do sprawdzenia")
    is_palindrome(input_from_prompt)

    
