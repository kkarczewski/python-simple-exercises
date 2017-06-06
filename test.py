
import random

def func(a):
    return a[::-1]

def wspak(a):
    a=a.split()
    a=a[::-1]
    return ' '.join(a)

def generuj():
    a = list()
    for one in range(1,7):
        a.append(random.randint(1,49))
    return a
def silnia(n):
    if n > 1:
        return n*silnia(n-1)
    else:
        return 1



    
if __name__ == '__main__':
    print(func('aabbbccc'))
    print(func([1,2,3,4,5]))
    print(wspak('ala ma kotaa'))
    print(generuj())
    print(silnia(5))
