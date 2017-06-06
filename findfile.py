#! /usr/bin/env python3.5
#! -*- coding: utf-8 -*-

import os

def findfile(name, path):
    finded = []
    for root, dirs, files in os.walk(path):
        if name in files:
            finded.append(os.path.join(os.path.abspath(root),name))
    return finded

if __name__ == '__main__':
    file_name = input("Podaj nazwę pliku")
    path_to_search = input("Podaj ścieżkę w której ma szukać")
    finded_files = findfile(file_name, path_to_search)
    for one in finded_files:
        print(one)
