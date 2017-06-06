# wyszukać w /root pliki .cfg i wszystkie README policzyć ile razem ich jest
# wyświetlić najdłuższą ścieżkę (największe zagnieżdżenie)
# największaa ilość znaków (/ -> to też znak)


import os, re, sys

def find_all_file(sciezka):	
    list_of_file = list()
    for root, subFolders,files in os.walk(os.path.abspath(sciezka)):
        for filein in files:
            if filein.endswith('.cfg') or filein == 'README':
                list_of_file.append(os.path.abspath(os.path.join(root,filein)))
    return list_of_file 	

def max_len_char(files):
    max = 0
    for one in files:
        if (len(one) > max):
            max = len(one)
            max_file = one
    return max, max_file

def depth_file_len(files):
    max = 0
    for one in files:
        #Rozróżnienie systemów ze względu na specyficzny zapis ścieżek
        #w windowsie. Nie wiem jak wygląda zapis ścieżki na mac'ach,
        #więc wyrzuciłem je do elsa jako niewspierane
        #TUTAJ ROZWIĄZANIE OPARTE O SYS.PLATFORM
        #Zakomentowane, bo nie sprawdzałem na linuxach
        #from sys import platform
        #if platform == "linux" or platform == "linux2":
        #    # linux
        #elif platform == "darwin":
        #    # OS X
        #elif platform == "win32":
        #    # Windows...
        #else:
        #    #Niespierane
        if os.name == 'nt': # windows
            one = one.split('\\')
        elif os.name =='posix': #linux (sprawdzone na debian,centos,redhat)
            one = one.split('/')
        else:
            print("System not supported")
            sys.exit(1)
        #Właściwe zliczanie i łączenie ścieżki
        if(len(one) > max):
            max = len(one)
            max_file = ('/').join(one)
    return max, max_file

if __name__ == '__main__':
    paths = find_all_file('C://')
    print('Liczba znalezionych plików:', len(paths))
    count_max, file_max = max_len_char(paths)
    print('Ilość znaków najdłuższej ścieżki:', count_max, 'dla pliku:', file_max)
    depth, depth_file = depth_file_len(paths)
    print('Największe zagłębienie ścieżki:', depth, 'dla pliku:', depth_file)
