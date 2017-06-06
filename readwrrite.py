#! /usr/bin/env python3.5
#! -*- coding: utf-8 -*-

import os
import sys

#CZYTANIE Z PLIKU
def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = [line.rstrip('\n') for line in file]
    except (IOError, OSError):
        print(sys.stderr, "\nFile dosn't exists or can't open file.")
        sys.exit(1)
    return lines

def read_file_as_one(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
    except (IOError, OSError):
        print(sys.stderr, "\nFile dosn't exists or can't open file.")
        sys.exit(1)
    return content

#ZAPIS DO PLIKU
def write_file(path_to_conf,file_name,data):
    if not os.path.exists(path_to_conf):
        os.mkdir(path_to_conf)
    try:
        with open(path_to_conf+file_name,'w') as fileout:
            fileout.writelines(data)
    except(IOError,OSError):
        print(sys.stderr, "\nCan't write to file.")
        sys.exit(1)

def count_lines(data):
    return len(data)

def count_words(data):
    words_count=0
    words = [one.split(' ') for one in data]
    for single_word in words:
        words_count += len(single_word)
    return words_count

def rewerse(data):
    letters = list()
    words = [one.split(' ') for one in data]
    for line in words[::-1]:
       new_line = list()
       for word in line[::-1]:
           new_line.append(word[::-1])
       new_line = (' ').join(new_line)
       new_line += '\n'
       letters.append(new_line)
    return letters

if __name__ == '__main__':
    # łatwiej się testuje z konsoli
    if len(sys.argv)>1:
        file_name = sys.argv[1]
    else:
        print("Input file name")
        file_name = input()
    lines = read_file(file_name)
    print("Number of lines:", count_lines(lines))
    print("Number of words:", count_words(lines))
    rewersed = rewerse(lines)
    print("Output file name")
    file_to_write = input()
    write_file('./', file_to_write, rewersed)


    print("TESTY")
    file = read_file_as_one(file_name)
    print(file[::-1])

    
