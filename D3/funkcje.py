# -*- coding: utf-8 -*-
import random
'''
def powitanie(imie):
    witaj = 'witaj '+imie
    return witaj

a = powitanie('Paweł ')
b = powitanie('Aleksander ')
c = powitanie('Janusz ')

print(a,b,c)
'''

'''
def powitanie(imie):
    witaj = 'witaj '+imie
    return witaj

L = []

for i in(range(1,4)):
    L.append(powitanie(input('podaj imię: ')))
print(L)
'''

#
'''
def dodawanie(a,b,imie='X',naz='Z'):
    wynik=a+b
    print(a,b)
    print(imie, naz)
    return wynik

res = dodawanie(a=14,naz=input('Y: '),b=24) #zamienia odpowiadające wartości na podane tutaj
print(res)
'''

'''
# implementacja !n
def silnia(n):
    res=1
    i=1
    L=[]
    while (i<=n):
        res*=i
        L.append(res)
        i+=1
    return L

def wyswietl(skl):
    for i in skl:
        print(i, end=' ')

wyswietl(silnia(4))
'''

'''
def f(n):
    F=[0,1]
    suma = 0
    i = 2
    suma = 0
    while (i<n):
        a = (F[i-2]+F[i-1])
        F.append(a)
        i+=1
    for i in F:
        suma = suma + 1
    return F[len(F)-1], suma, F

Fib = f(6)
print('(element, suma, kolejne elenemty)', Fib)
'''

'''
def f(n):
    for i in range(0, n):
        a, b = b, a + b
    return a
'''

'''
def s(a=5):
   # los = ['oko','dom','piec','torba','piłka']
    los = ['oko','oko','piec','oko','oko']
    
    i=0
    Z = []
    while (i<a):
        Z.append(los[random.randint(0,len(los)-1)])
        i +=1
    return Z
print(s())
'''

'''
#
import math

def odl(x1,y1,x2,y2):
    wz = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
    return round(wz,2)

print(odl(2,4,6,8))
'''

#odległość v.2
import math

def odl(x1,y1,x2,y2):
    wz = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
    return round(wz,2)
i = 0
x = []
y = []

while (i < 2):
    if (i == 1):
        print('położenie końcowe: ')
    else:
        print('położenie początkowe: ')
    x1 = int(input(''))
    y1 = int(input(''))
    x.append(x1)
    y.append(y1)
    i = i + 1
print('odległość: ', odl(x[0],y[0],x[1],y[1]))

