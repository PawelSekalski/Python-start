# -*- coding: utf-8 -*-
# polskie znaki, trzeba zapisać w każdym skrypcie osobno


'''# po kratce komentarz w jednej linii

"""
komantarz blokowy. trzy apostrofy rozpoczynaja i trzy apostrofy koncza

"""

zmienna1 = 5.0
zmienna2 = 5.3
witaj = 'siemacotam'

tekst1 = "to jest moj tekst"
tekst2 = 'moze byc apostrofa'
literki1 = 'A'
literki2 = "a"

# zeby w zdaniu mogla sie pojawic apostrofa, zdanie nalezy zapisac w cudzyslowiu

# w zmiennych duza i mala litera to zupelnie inne znaki
# w nazwie zmiennych nie moze byc spacji

zmienna3 = 2 + 4
Zmienna3 = 'liczba'

nowa_zmienna = (zmienna3+5)

print(zmienna1)
print(witaj)
print(zmienna1, zmienna2)
print(zmienna3, Zmienna3)
print(nowa_zmienna)
print("Hi, "+ witaj)

print("Hi, "+ tekst2 + ".")

# slowa kluczowe zawsze sa zaznaczone na niebiesko
 
# zmienne nie moga sie zaczynac od cyfr, ale od znakow nieliterowych juz tak

# w trakcie mozna zmienic wartosc zmiennej. kazda nastepna zmienia poprzednia, ale tylko dla zapisow za nia
print("przed zmiana:", Zmienna3)
Zmienna3 = 3.14
print("po zmianie:", Zmienna3)


del zmienna1
#print(zmienna1)
'''

'''
#1
a = 1
b = "2, 4"
c = "w1"

#2
a = "2.1"
b = "abc"
c = 0

print(a, b, c)
'''

'''
#3
imie = input("podaj imię: ")
nazwisko = input("podaj nazwisko: ")
rok_urodzenia = input("podaj datę urodzenia: ")
stanowisko = input("podaj stanowisko: ")
placa = input("wynagrodzenie: ")
print(imie, nazwisko, rok_urodzenia, stanowisko, placa)
'''

'''  
#4 pi r2
pi = 3.14
r = 8
pole_kola = pi * r * r

# podstawa ** wykladnik

print(pole_kola, pi*(r**2))
'''
'''
#4.1
pi = 3.14
# int() rzutuje na intiger
# input() czyta wartość z klawiatury - string!
promien = int(input("podaj liczbę"))
pole_kola = pi * promien * promien

# podstawa ** wykladnik

print(pole_kola, pi*(promien**2))


# brak wartości - none

# type() zwraca typ wartości zmiennej
print(type(pole_kola))
print(type(21j))
'''

'''
dluga = 5197512332
print(type(dluga))
'''

'''
dluga2 = 32l
print(type(dluga2))
'''
'''
# // odpowiednik flor w sql
print(3/2, 3//2)

# zaokrąglanie round(liczba, precyzja)
print(round(2.134445, 2))
print(round(-2.134445, 2))

#int obcina końcówki
print(int(1.3),int(1.5),int(1.9))
'''

'''
#P10
netto = float(input("Kwota netto: "))
vat = int(input("Stawka VAT (3%, 7%, 23%): "))
brutto = netto + (netto*(vat/100))
print("Kwota netto przy stawce" +str(vat)+ "VAT wynosi: " +str(brutto)+ "zł")
'''

'''
#P11 paragon
nazwa_p1 = "chleb"
nazwa_p2 = "mleko"
nazwa_p3 = "cukierki"

cena_p1 = 1.99
cena_p2 = 3.15
cena_p3 = 20.99

zamowienie_p1 = int(input("chleb (szt.): "))
zamowienie_p2 = float(input("mleko (l): "))
zamowienie_p3 = float(input("cukierki (g): "))
suma = (cena_p1 * zamowienie_p1) + (cena_p2 * zamowienie_p2) + ((cena_p3/1000) * (zamowienie_p3))

print("zamówienie")
print("_____________")
print("liczba sztuk chleba", zamowienie_p1, "szt.")
print("ilość litrów mleka:", zamowienie_p2, "L")
print("waga cuierków:", zamowienie_p3, "g")
print("_____________")
print("Do zapłaty")
print("_____________")
print(round(suma, 2), "zł")
'''

'''
print(a*b)
log1=True
print(type(log1))
'''

'''
print(bool(""), bool(0), bool("Ala"))
'''

'''
a = """
autor:
data:
wersja:
"""
print(a)
'''

'''
# \n znak przejścia do nowej linii
b = "autor:\ndata:\nwersja:"
print (b)

txt = "\nnapis"
print(txt*2)
'''

'''
#
imie = input("imię: ")
imie1 = imie + ", \n"
imie2 = imie + "."
n = int(input("Podaj krotność imienia: "))
print((imie1 * (n-1)) + imie2)
'''

'''
# 
imie = input("imię: ")
nazwisko = input("nazwisko: ")
wiek = input("wiek: ")
stanowisko = input("stanowisko: ")
pensja = input("pensja: ")

print(imie, nazwisko, "(" + "wiek: " + wiek + ")", "pracuje na stanowisku: " + stanowisko, "(" + "pensja: " + pensja + " zł" + ")")
'''

'''
#print((imie_1 * (n-1) + imie_2)
a = 1
print(type(a))
napis = str(a)
print(type(napis))
'''

#//////////////////////////////////////////////////OPERATORY
'''
#P25
kwota_netto = 5500 / 168
print("stawka godzinowa netto", round(kwota_netto,2), "zł")
print("stawka godzinowa brutto", round(kwota_netto * 1.23,2), "zł")
'''

'''
# P26 prawo De Morgana
# ~/p and q) <=> (~p or ~q)
p = True
q = True
dM1 = not (p and q)
dM2 = (not p) or (not q)
print(dM1, dM2)
print(dM1 == dM2)
'''

'''
# P27
a = True
b = False
c = False
# and, or
'''

'''
pierwszy = (not a) and (not b) and (not c)
drugi = (not a) and (not b) and c
trzeci = (not a) and b and (not c)
czwarty = a and (not b) and (not c)
z = pierwszy or drugi or trzeci or czwarty
print(z)
'''

'''
# > < == >= <= != is[not] 
print('ala' > 'alarm')
'''

'''
#P28
liczba = round(17**(1/2),2)
uroj = 1j
print(liczba * uroj)

liczba = round(17**(1/2),2)
uroj = 1j
res = str (liczba * uroj)
print("liczba zespolona: 0 + "+res)
'''

'''
# P29 potęga **
Z = 17 % 7
print(Z**2 + 3*Z)
'''

'''
# P30
print(((str(1.2e+3+34.5) + "; ") * 20))
      
print(((str(1.2e+3+34.5) + "; ") * 19) + str(1.2e+3+34.5) + ".")

w1 = 1.2e+3+34.5
print(((str(w1) + "; ") * 19) + str(w1) + ".")
'''

'''
# 32
q1 = input("napis 1: ")
q2 = input("napis 2: ")
print("napis 1 jest większy leksykograficznie", q1 > q2)
print("napisy są równie", q1 == q2)
print("napis 2 jest większy leksykograficznie", q1 < q1)
'''

'''
# nagłówek
print("imię\t"+"nazwisko\t"+"stanowisko")
'''

# procent składany, kapitalizacja roczna
SPK = int(input("Podaj SPK "))
P = float(input("Podaj procent składany "))
N = int(input("Podaj liczbę lat "))
res = round(SPK*(1+(P/100))**N, 3)
print("Kwota po " + str(N) + " latach wynosi: " + str(res) + " zł")

#