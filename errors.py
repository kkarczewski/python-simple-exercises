import os

def attr_err(a):
    try:
        # Nie mam pomysłu co tutaj wrzucić, żeby wymusić powstanie
        # wyjątku do wyłapania
        print(a)
    except AttributeError as e:
        print(a, e)

def index_err(a):
    try:
        # Nie mam pomysłu co tutaj wrzucić, żeby wymusić powstanie
        # wyjątku do wyłapania
        print(a)
    except IndexError as e:
        print(a, e)

def os_err(a):
    try:
        # Nie mam pomysłu co tutaj wrzucić, żeby wymusić powstanie
        # wyjątku do wyłapania
        print(a)
    except OSError as e:
        print(a, e)

def runtime_err(a):
    try:
        # Nie mam pomysłu co tutaj wrzucić, żeby wymusić powstanie
        # wyjątku do wyłapania
        print(a)
    except RuntimeError as e:
        print(a, e)

def my_own(a):
    try:
        # Nie mam pomysłu co tutaj wrzucić, żeby wymusić powstanie
        # wyjątku do wyłapania
        raise(a)
    except Exception as e:
        print(a, e)

if __name__ == '__main__':
    attr_err('Attr Error')
    index_err('Index Error')
    os_err('OS Error')
    runtime_err('Runtime Error')
    my_own('My Error')
