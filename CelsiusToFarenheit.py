def c_to_f(c):
    return c*1.8 + 32

def f_to_c(f):
    return (f-32)/1.8

if __name__ == '__main__':
    i=True

    while(i):
        choose = input("If F to C type 0 if, C to F type 1, if quit type Q\n")
        if (choose=='0'):
            numb = input("Type temp\n")
            print(f_to_c(float(numb)))
        elif (choose=='1'):
            numb = input("Type temp\n")
            print(c_to_f(float(numb)))
        elif (choose=='Q' or choose=='q'):
            print('Quit')
            i=False
        else:
            print("Czego nie rozumiesz?! 0, 1 lub Q! Nie kombinuj!")
