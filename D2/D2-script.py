# -*- coding: utf-8 -*-

# D2
# SŁOWNIK
import random

'''
literki = {'a' : 'A', 'b' : 'B', 'c' : 'C'}
print(literki)

print(literki.keys(), literki.values())
literki['d'] = 'D'
del literki ['c']
literki[2] = 'abc'
print(literki)
to_str = str(literki)
print(to_str[0], to_str[1])
'''

'''
# P44
key1 = input('Podaj liczbę (1-5) zapisaną słownie: ')

to_dec = {'jeden':1, 'dwa':2, 'trzy':3, 'cztery':4, 'pięć':5}

print(key1.capitalize() + ' w postaci dziesiętnej to: ' +str(to_dec[key1]))
'''

'''
# P47
key1 = input('Podaj liczbę (1-5) zapisaną słownie: ')

s1 = {'jeden':1, 'dwa':2, 'trzy':3, 'cztery':4, 'pięć':5}
s2 = {1:'I', 2:'II', 3:'III', 4:'IV', 5:'V'}

print('Dla ' + key1 + ' postać dziesiętna: ' + str(s1[key1]) + ', postać rzymska: ' + str(s2[s1[key1]]))
'''

'''
# P48
key = input('Produkty (z, mleko, papier): ')
ilosc = int(input('Ilość: '))
towar = {'z':1, 'mleko':2, 'papier':3}
cena = {1:5, 2:10, 3:1000}
print('Suma: ' + str(round(cena[towar[key]]*ilosc,2)) + 'zł (netto), '+str(round(cena[towar[key]]*ilosc*1.23,2))+ 'zł (brutto)')
'''

# ZBIORY
'''
ksztalty = set(['koło', 'kwadrat', 'trójkąt'])
ksztalty.add('okrąg')
ksztalty.discard('koło')

okragle = set(['koło'])
print(len(ksztalty), len(okragle))

print(ksztalty)
print(okragle)

print(ksztalty.issubset(okragle))
print(ksztalty.issuperset(okragle))
print(ksztalty | okragle)
print(ksztalty & okragle)
print(ksztalty - okragle)
print(ksztalty ^ okragle)
'''

# random

'''
import random
los = random.randint(1,49)
print(los)

s = set()
s.add(random.randint(1,49))
s.add(random.randint(1,49))
s.add(random.randint(1,49))
s.add(random.randint(1,49))
s.add(random.randint(1,49))
s.add(random.randint(1,49))
l = list(s)
print(l[:6])
'''

#//////////////////////////////////////////////////////////////////INSTRUKCJE WARUNKOWE
'''
if (warunek):
    instrukcja

elif (warunek):
    instrucja   

else (warunek):
    instrukcja
'''

'''
a = int(input("Podaj liczbę parzystą: "))

if (a%2 == 0):
    print("Liczba "+str(a)+' jest parzysta.')
    print('Gratulacje, potrafisz rozróżniać cyfry')
else:
    print("Liczba " +str(a)+' nie jest parzysta')
    print('Gratulacje, nie potrafisz rozróżniać cyfr')
print ('jestem już za instrucją "if"')
'''

'''
a = int(input("Podaj liczbę parzystą: "))

if (a%2 == 0):
    print('Liczba '+str(a)+' jest parzysta.')
    if(a >= 10):
        print(':iczba '+str(a)+ ' jest parzysta i większa od/równa 10')
    else:
        print('Liczba '+str(a)+ ' jest parzysta i mniejsza od 10')
else:
    print('Liczba ' +str(a)+' nie jest parzysta')

print ('jestem już za instrucją "if"')
'''

'''
a = int(input("Podaj liczbę parzystą: "))

if (a%2 == 0 and a >= 10):
    print(':iczba '+str(a)+ ' jest parzysta i większa od/równa 10')
elif (a%2 == 0 and a < 10):
    print('Liczba '+str(a)+ ' jest parzysta i mniejsza od 10')
else:
    print('Liczba ' +str(a)+' nie jest parzysta')

print ('jestem już za instrucją "if"')
'''

'''
a = int(input("Podaj liczbę parzystą: "))

if (a%2 == 0 and a >= 10):
    print('Liczba '+str(a)+ ' jest parzysta i większa od/równa 10')
elif (a%2 == 0 and a < 10):
    print('Liczba '+str(a)+ ' jest parzysta i mniejsza od 10')
else:
    print('Liczba ' +str(a)+' nie jest parzysta')

print ('jestem już za instrucją "if"')
'''

# P53
'''
if (bool(0)):
    print(bool(0))
if (bool(1)):
    print(bool(1))
if (bool(2)):
    print(bool(2))
if (bool(3)):
    print(bool(3))
if (bool(4)):
    print(bool(4))
'''

# P54
'''
a = int(input("Podaj liczbę w przedziale 0-9: "))
if (a >= 0 and a <= 9):
    print("Liczba w przedziale")
else:
    print("Poza przedziałem")
'''

'''
# P55
lista = [1,2,3,4,5,6,7,8,9]
a = int(input("Podaj cyfrę: "))    
if (a >= 0 and a <= (len(lista)-1)):
    print("Index: " +str(lista[a]))
else:
    print("Poza przedziałem")
'''

# P55
'''
lista = [0, 1]
if(lista[0]>0 and lista [1]>0):
    print('oba elementy dodatnie')
elif(lista[0]>0 and lista [1]<=0):
    print('pierwszy element dodatni, drugi nie')
elif(lista[0]<=0 and lista [1]>0):
    print('drugi element dodatni, pierwszy nie')
else:
    print('żaden element nie jest dodatni')    
'''

# P56
'''
a = set([1, 3, 4, 5])
b = set([1, 3, 4])
if (a.issuperset(b)):
    print('a jest nadzbiorem b')
else:
    print('b jest nadzbiorem a')

 
a = set([1, 3, 5])
b = set([1, 3, 5])  
if(a==b):
    print('zbiory równe')
elif (a.issuperset(b)):
    print('b jest nadzbiorem a')
elif (b.issuperset(a)):
    print('b jest nadzbiorem a')
else:
    print('zbiory są różne')
'''   
    
'''
lista = [1,2,3,4,5,6,7,8]
i = 0
while(i <= (len(lista)-1)):
    print('Index: ' +str(i)+'\t wartość: '+str(lista[i]))
    i+=1
    
print('poza pętlą')
'''

'''
lista = [1,2,3,4,5,6,7,8]
i = 0
while(i <= (len(lista)-1)):
    if(lista[i]%2 == 0):
        print('Index: ' +str(i)+'\t wartość: '+str(lista[i]))
    i+=1

print('----------LUZZTRO----------')
lista = [1,2,3,4,5,6,7,8]
i = len(lista) -1
while(i > 0):
    if(lista[i]%2 == 0):
        print('Index: ' +str(i)+'\t wartość: '+str(lista[i]))
    i-=1
'''

'''
lista = [1,2,3,4,5,6,7,8]
i = len(lista) -1
while(i > 0):
    if(lista[i]%2 == 0):
        print('Index: ' +str(i)+'\t wartość: '+str(lista[i]))
    i-=1
else:
    print('jestem w else')
    
print('jestem poza')
'''

# WYRAŻENIE TRÓJARGUMENTOWE
# która z liczb jest większa i o ile większa
'''
A = 8765
B = 4123
print('A > B o: ' +str(A-B)) if (A>=B) else print('A < B o: ' +str(B-A))
'''


# Pętla for-in sortowanie w listach
'''
lista = [1,2,3,4,5,6,7,8]
for v in lista:
    print('wartość: ' +str(v))
'''

'''
lista = [1,2,3,4,5,6,7,8]
for index, var in enumerate(lista):
    print('index: '+str(index)+'\twartość: '+str(var))
'''

# for-in słownik, literowanie po kluczach
'''
słownik = {'a':1, 'b':2, 'c':3}
for k in słownik:
    if(słownik[k] >=2):
        print(k, słownik[k])
'''

# range
'''
lista = range(10)
print(lista)
for i in lista:
    print(i)
'''

'''
for j in range(15,25):
    print(j)
'''

'''
for k in range(0,50,2):
    print(k, k**2, k+5)
'''

# formatowanie długości wyjścia z programu
'''

for k in range(0,50,2):
    print(k, k**2, k**3)
'''

# pojedyncze i zastępuje intiger
'''
for k in range(0,100):
    print('wynik: %4i%6i%8i' % (k, k**2, k**3))

for l in range(0, 100):
    print('pierwiastek kwadratowy z %4i wynosi: %6f.2f' % (l, l**0,5))
'''
  
# 57
'''
zam=input("Zamówienie: ")
sklep_prod = {'nic':1, 'nic2':2, 'nic3':3}
prod_dost = {1:5, 2:2, 3:7}
if(zam in sklep_prod.keys()):
            if(zam == a and prod_dost[sklep_prod[a]] >= zam):
                        print('dostępne: ' + a)
                        print('zamawiasz: ' + str(zam_il) + ' szt.')
            elif(prod_dost[sklep_prod[a]] < zam_il):
                        print('produkt dostępny: ' + a)
                        print('dostępne tylko: ') + str(prod_dost(sklep_prod[a]) + ' szt.')
            else:
                        print('brak dostępności towaru')
''' 
                      
'''               
elif(zam == a and prod_dost[sklep_prod[a]] < zam_il):

elif(zam == a and prod_dost[sklep_prod[a]] < zam_il):
      print('towar dostępny: ' + a)
      print('dostępne: ' + str(prod_dost[sklep_prod[a]]) + ' szt.')
else:
      print('brak towaru, który chcesz zamówić')
'''

'''
sklep_prod = {'nic':1, 'nic2':2, 'nic3':3}
prod_dost = {1:5, 2:2, 3:7}
prod_cena = {1: 500, 2: 444, 3: 1}
suma = 0
i = 't'
while(i == 't'):
      zam = input('wybierz towar: ')
      zam-il = int(input('podaj ilość: '))
      if (zam in sklep_prod.keys()):
                  if
      (zam == a and prod_dost[sklep_prod[a]] >= zam_il):
                        print('dostępne: ' + a)
                        print('zamawiasz: ' + str(zam_il) + ' szt.')
                  elif(prod_dost[sklep_prod[a]] < zam_il):
                        print('produkt dostępny: ' + a)
                        print('dostępne 
'''


# P60
'''
i='t'
lista = []
slownik = {'0':'zero', '1':'jeden', '2':'dwa', '3':'trzy', '4':'cztery', '5':'pięć', '6':'sześć', '7':'siedem', '8':'osiem', '9':'dziewięć'}
while(i == 't'):
    cyfra = input("wprowadź cyfrę: ")
    if(cyfra.isdigit()):
        lista.append(slownik[cyfra])
    else:
        print('wartość nie jest cyfrą')
    i = input('następna cyfra? t/n ')
print(lista)
for i in lista:
    print(i,'',end="")
'''

#61
'''
a = range(1,11)
b = 1
while (b <= 10):
    print('%3i%3i%3i%3i%3i%3i%3i%3i%3i%3i' % (b*a[0], b*a[1], b*a[2], b*a[3], b*a[4], b*a[5], b*a[6], b*a[7], b*a[8], b*a[9]))
    b+= 1
'''

lp = range(1,10,2)
a = len(lp) -1 # malejąco
while (a >= 0):
    print(lp[a])
    a -= 1
    
lp = range(1,10,2)
a = len(lp) -1 # malejąco
while (a >= 0):
    print(lp[a]**2)
    a -= 1
    