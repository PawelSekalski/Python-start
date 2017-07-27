# -*- coding: utf-8 -*-
import random
'''
class [nazwa klasy]:
    pola
    def nazwaMetody([argumenty]):
        for v in 
        while (warunek): - pętle
            if(warunek)
            elif         - funkcje warunkowe
            else:
nazwa obiektu = nazwa klasy()
'''
'''
class PierwszaKlasa:

    def __init__(self,x,y):
        self.x = x
        self.y = y        
    def witaj(self):
        print('witaj w metodzie klasy')
    def dodaj(self, x, y):
        print('dodawanie ')
        return self.x + self.y
    def odejmij(self):
        print('odejmowanie ')
        return self.x - self.y
  
print('pierwszy obiekt') 
obiekt1 = PierwszaKlasa(7,6)
obiekt1.witaj()
print(obiekt1.dodaj(6,7))
print(obiekt1.odejmij())

print('drugi obiekt')
obiektDwa = PierwszaKlasa(8,9)
obiektDwa.witaj()
print(obiektDwa.dodaj(16,77))
print(obiektDwa.odejmij())
'''

'''
class PierwszaKlasa:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.dodaj()
        self.odejmij()
    def dodaj(self):
        self.wynik_d = self.x + self.y
        return self.wynik_d
    def odejmij(self):
        self.wynik_o = self.x - self.y
        return self.wynik_o
    def __str__ (self):
        return 'wynik dodawania = '+str(self.wynik_d)+'; wynik odejmowania = '+str(self.wynik_o)
  

obiekt = PierwszaKlasa(7,6)
print(obiekt)
'''


# dodawanie
'''
class PierwszaKlasa:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.dodaj()
        self.odejmij()
    def dodaj(self):
        self.wynik_d = self.x + self.y
        return self.wynik_d
    def odejmij(self):
        self.wynik_o = self.x - self.y
        return self.wynik_o
    def __str__ (self):
        return 'wynik dodawania = '+str(self.wynik_d)+'; wynik odejmowania = '+str(self.wynik_o)
    def __add__(self,other):
        return self.x + other.x, self.y + other.y
    def __ge__ (self,other): #operator dwuargumentowy - porównanie
        return self.x >= other.x, self.y >= other.y

o1 = PierwszaKlasa(1,6)
print(o1)
o2 = PierwszaKlasa(3,2)
#rzutowanie z __str__
print(o2)
#rzutowanie z __add__
print(o1 + o2)
#rzutowanie z __ge__
print(o1 >= o2)

'''
#BMI=waga/(wzrost/100)**2
'''
class BMI:
    def __init__(self, imie, nazwisko, waga, wzrost):
        self.imie = imie
        self.nazwisko = nazwisko
        self.waga = waga
        self.wzrost = wzrost
        self.oBMI()
    
    def oBMI(self):
        self.bmi = round(self.waga/((self.wzrost/100)**2))
    
    def __str__ (self):
        return 'BMI zawodnika '+self.imie+' '+self.nazwisko+' wynosi: '+str(self.bmi)

zawodnik = BMI('Jerzy', 'Ponton', 180, 170)
print(zawodnik)
'''

'''
class Sklep:
    def __init__(self, towar, cena, ilosc):
        self.towar_klasa = towar
        self.cena_klasa = cena
        self.ilosc_klasa = ilosc
        self.zaplata_calk = self.zaplata()*1.23
        
    def zapłata(self):
        do_zaplaty = self.cena_klasa * self.ilosc_klasa
        return do_zaplaty
zakup1 = Sklep('chleb', 3.99, 4)
print(self.towar_klasa)
print(self.cena_klasa)
print(self.ilosc_klasa)
zakup1.ilość = 5
print(zakup1.ilosc_klasa)
print(zakup1.zaplata())
print(zakup1.zaplata_calk)
'''
        # for v in range(1,7): nie potrzebne przy sample

# symulator Lotto
class Lotto:
    def __init__(self):
        print(random.sample(range(1,50),6))

los1 = Lotto()
los2 = Lotto()
los3 = Lotto()
los4 = Lotto()
los5 = Lotto()
los6 = Lotto()
