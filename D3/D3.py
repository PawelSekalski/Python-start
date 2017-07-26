# -*- coding: utf-8 -*-

'''
x = int(input('x '))
y = int(input('y '))
i = 1
res = 1
while(i<=y):
    res *= x
    i +=1
    print(res)
'''
"""
#
'''
n = int(input('n '))
a1 = float(input('a1 '))
q = float(input('q '))
'''
n = 5
a1 = 6
q = 4
i = 0
S = 0
L = []
while (i < n):
    S = S + (a1* (q**i))
    i += 1
    L.append(S)
'''
    print('Suma: ', S)
    print('Składniki: ', L)#print(a1*(q**(n-1)))

for i in L:
    print(i, end=" ")
'''
print('%-10s %14.2f' % ('Suma:', S))
print('%-10s' % ('Składniki:'), end=" ")
for i in L:
    print('%14.2f' % (i), end=" ")
"""
'''
# szukanie i licznie wybranych znaków
#len - literowanie 
napis = input('Napis: ')
szukaj = input('podaj szukaną literę: ')
i = 0
licznik = 0
while (i <= len(napis) -1):
    if(napis[i] == szukaj):
        print('znaleziono ', szukaj, ' na pozycji ', i+1)
        licznik +=1
    i += 1
print('znaleziono',licznik,'razy')
'''
'''
# szukanie par znaków
napis = input('Napis: ')
szukaj = input('podaj szukaną literę: ')
i = 0
licznik = 0
while (i <= len(napis) -1):
    n=napis[i:i+len(szukaj)]
    if(n == szukaj and napis[i+1] != szukaj[0]):
        print('znaleziono ', szukaj, ' na pozycji ', i+1)
        licznik +=1
    i += 1
print('znaleziono',licznik,'razy')
'''

'''
#v.2
napis = input('Napis: ')
szukaj = input('podaj szukaną literę: ')
i = 0
licznik = 0
while (i <= len(napis) -1):
    n=napis[i:i+len(szukaj)]
    if(n == szukaj):
        print('znaleziono ', szukaj, ' na pozycji ', i+1)
        licznik +=1
        i = i + len(szukaj)
    else:
        i += 1
print('znaleziono',licznik,'razy')
'''

# C na F tabela, zakres
'''
start = int(input('start: '))
stop = int(input('stop: '))
step = int(input('step: '))
while(stop - step<start):
    print('zbyt duży krok')
    step=int(input('step: '))
C= range(start,stop + step,step)
i = len(C)-1
print('%7s | %7s' % ('C', 'F'))
while (i >= 0):
    if(C[i] ==0):
        print('-----------------------------')
        print('%7i | %7.1f' % (C[i], (C[i]*1.8)+32))
        print('-----------------------------')
    else:
        print('%+7i | %7.1f' % (C[i], (C[i]*1.8)+32))
    i-=1
'''
'''
# v.2
start = int(input('start: '))
stop = int(input('stop: '))
step = int(input('step: '))
if((stop - start) % step ==0):
    C=range(start,stop+step,step)
else:
    C= range(start,stop,step)
i = len(C)-1
print('%7s | %7s' % ('C', 'F'))
while (i >= 0):
    if(C[i] ==0):
        print('-----------------------------')
        print('%7i | %7.1f' % (C[i], (C[i]*1.8)+32))
        print('-----------------------------')
    else:
        print('%+7i | %7.1f' % (C[i], (C[i]*1.8)+32))
    i-=1
'''

#kalkulator F/C
'''
x = input("F/C? ")
if x == "f":
    y = (input("ile F? "))
    f = (int(y) - 32) / 1.8
    print(f, "C")
if x == "c":
    n = input("ile C? ")
    c = ((int(n) * 1.8) + 32)
    print (c, "F")
'''

#

D = ['2', '3', '3.5', '4', '4.5', '5']
print('wpisz ocenę: ')
i = 'x'
oceny = []
while (i != ''):
    i = input(' ')
    if(i in D):
        oceny.append(float(i))
    elif(i ==''):
        print('oceny wprowadzone')
    else:
        print('ocena niepoprawna')
so=0
print('-----------------')
for i in oceny:
    so += i
print('średnia ocen', round(so/len(oceny),2))
