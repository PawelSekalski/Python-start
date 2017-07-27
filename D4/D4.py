# -*- coding: utf-8 -*-
import random

# P75
'''
def s (*arg):
    s = 0
    avg = 0
    for v in arg:
        s += v
        avg = s/len(arg)
    return avg

print(s(5,7,9))
print(s())
'''


# P74-002
'''
def wykres(d, x ='*', ilosc=2):
    v = 0
    wart = []
    if (d =='M' or 'm'):
        while(v < ilosc):
            wart.append(int(input('podaj liczbę: '+str())))
            v += 1
    elif (d == 'A' or 'a'):
        while(v < ilosc):
            wart.append(random.randint(0,9))
            v += 1
    for c in wart:
        print(x * c)

def menu():
    x_menu = input('znak: ')
    ilosc_menu = input('ilość: ')
    dec = input('tryb: A - auto, M - manual ')
    if (x_menu == '' and ilosc_menu != ''):
        wykres(d=dec, ilosc = int(ilosc_menu))
    elif(x_menu != '' and ilosc_menu == ''):
        wykres(d=dec, x = x_menu)
    elif(x_menu !='' and ilosc_menu !=''):
        wykres(dec, x_menu, int(ilosc_menu))
    else:
        wykres(d=dec)

menu()
'''

'''
#
def htmlexp(napis,color='orange',size='10px',weight='8'):
    return '<span style="color: '+color+'; font size: '+size+'; fornt weight: '+weight+'"> '+'\n'+napis+'</span>'
print(htmlexp('hello world!'))
'''

#P74
'''
kolor = 'black cat' or 'white rabbit'
licznik = 0
licznik_b = 0
licznik_w = 0
def klik():
    global kolor
    global licznik, licznik_b, licznik_w
    licznik += 1
    if (kolor == 'white rabbit'):
        kolor = 'black cat'
        licznik_b += 1
    elif (kolor =='black cat'):
        kolor = 'white rabbit'
        licznik_w += 1
    return kolor
print(klik())
print(klik())
print(klik())
print(klik())
print(klik())
print(klik())
print(klik())
print('razem:',licznik)
print('czarne:', licznik_b)
print('białe:', licznik_w)
'''

#74(120)
'''
def dodawanie(a,b):
    return a+b
def odejmowanie(a,b):
    return a-b
def mnożenie(a,b):
    return a*b
def dzielenie(a,b):
    return a/b
def menu():
    x = ""
    while (x != "q"):
        x = input('dodawanie (+), odejmowanie (-), mnożenie (*), dzielenie (/), (Q) wyjście: ')
        if(x == '+'):
            print('wynik =',dodawanie(int(input('a=')),int(input('b='))))
        elif(x == '-'):
            print('wynik =',odejmowanie(int(input('a=')),int(input('b='))))
        elif(x == '*'):
            print('wynik =',mnożenie(int(input('a=')),int(input('b='))))
        elif(x == '/'):
            print('wynik =',dzielenie(int(input('a=')),int(input('b='))))            
        elif(x != '+' and x != '-' and x == 'q'):
            print('to nie!')
menu()
'''

# P74

'''
def sumaT(tab):
    tab = []
    v = 't'
    print('liczby: ')
    while(v != ' '):
        v=float(input(' '))
        if(v != ' '):
            tab.append(float())
        elif(v ==' '):
            print('wprowadzono')
    print(tab)
'''

def spr():
    tab = []
    v = 'x'
    print('liczby: ')
    while(v != ''):
        v = input('')
        if(v != ''):
            while True:
                try:
                    v = float(v)
                    break
                except ValueError:
                    print('błąd! podaj liczbę')
                    v = input (' ')
            tab.append(v)
        elif(v==''):
            print('wprowadzono')
            print(tab)
            return tab
def wypisz5(limit,lista):
    print('elementy większe niż 5'+str(limit))
    suma = 0
    for v in lista:
        if (v >= limit):
            print(v, end=' ')
            suma += v
    print('suma: ',suma)
wypisz5(int(input('podaj odcięcie: ')),spr())