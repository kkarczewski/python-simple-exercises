#! /usr/bin/env python3.5
#! -*- coding: utf-8 -*-

import os
#import sys
import shutil
import errno

def print_help():
    print('''Opcje do wyboru:
‘L’ – lista elementow w bierzacym katalogu
‘O’ – otworz katalog (inaczej cd katalog)
‘U’ – utworz plik
‘C’ – utworz katalog
‘R’ – usun plik/katalog (tutaj uwazajcie na niepuste katalogi)
‘M’ – zmien nazwe
‘P’ – skopiuj
DORZUCIŁEM OD SIEBIE "Q" żeby obsłużyć sygnał wyjścia z programu''')
    
def is_first_time(is_first):
    if is_first:
        print_help()
        letter = input("Wybierz opcję")
    else:
        letter = input("Wybierz opcję")
    return letter, False

#Rozwiązanie dla uruchomienia z konsoli w linuxie
#Wystarczy przekazywać odpowiednią komendę do funkcji.
def action(cmd):
    os.system(cmd)

#‘L’ – lista elementow w bierzacym katalogu
def ls():
    elements = os.listdir()
    for one in elements: print(one)    

#‘O’ – otworz katalog (inaczej cd katalog)
def cd():
    path = input("Podaj ścieżkę")
    try:
        os.chdir(path)
        print("IN:", os.getcwd())
    except OSError as e:
        print(e)

#‘U’ – utworz plik
def touch():
    name = input("Podaj nazwę pliku")
    try:
        open(name, 'x').close()
    except OSError as e:
        print(e, 'or file exists!')        

#‘R’ – usun plik/katalog (tutaj uwazajcie na niepuste katalogi)
def rm(): 
    name = input("Podaj ścieżkę do pliku/katalogu")
    try:
        os.remove(name)
    except:
        try:
            os.rmdir(name)
        except:
            try:
                shutil.rmtree(name)
            except OSError as e:
                print(e) 

#‘C’ – utworz katalog
def mkdir():
    path = input("Podaj nazwę katalogu lub nazwę ze ścieżką")
    try:   
        os.makedirs(path)
    except OSError as e:
        print(e)

#TO DO:: OBSŁUGA BŁĘDU ŚCIEŻKI
def mv():
    src = input("Podaj ścieżkę do pliku który chcesz zmienić")
    dst = input("Podaj nową nazwę pliku")
    try:
        os.rename(src,dst)
    except OSError as e:
        print(e)

#‘P’ – skopiuj
def cp():
    src = input("Podaj ścieżkę do kopiowanego pliku/katalogu")
    dst = input("Podaj ścieżkę do katalogu docelowego")
    try:
        shutil.copytree(src, dst)
    except OSError as e:
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else:
            print('Directory not copied. Error: %s' % e)

def file_manager(is_first):
    again = True
    while(again):
        letter, is_first = is_first_time(is_first)
        if letter=='l' or letter=='L':
            #‘L’ – lista elementow w bierzacym katalogu
            ls()
        elif letter=='o' or letter=='O':
            #‘O’ – otworz katalog (inaczej cd katalog)
            cd()
        elif letter=='u' or letter=='U':
            #‘U’ – utworz plik
            touch()
        elif letter=='c' or letter=='C':
            #‘C’ – utworz katalog
            mkdir()
        elif letter=='r' or letter=='R':
            #‘R’ – usun plik/katalog (tutaj uwazajcie na niepuste katalogi)
            rm()
        elif letter=='m' or letter=='M':
            #‘M’ – zmien nazwe
            mv()
        elif letter=='p' or letter=='P':
            #‘P’ – skopiuj
            cp()
        elif letter=='q' or letter=='Q':
            again = False
        else:
            print("Czego nie rozumiesz? Wybierz z opcji, nie wymyślaj.")

if __name__ == '__main__':
    file_manager(True)
