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



'''
# Lotto v.2
class Lotto:
    def __init__(self):
        self.L = (range(1,50))
        self.tab=random.sample(self.L,6)
        print(self.tab)

los1 = Lotto()
los2 = Lotto()
los3 = Lotto()
los4 = Lotto()
'''

# Lotto i sortowanie
'''
class Lotto:
        def __init__(self):
                self.L = range(1,50)
                self.tab=random.sample(self.L,6)
                self.sorted()
        def sorted(self):
                self.tab_sorted=sorted(self.tab)
                print(self.tab_sorted)
los1 = Lotto()
los2 = Lotto()
los3 = Lotto()
los4 = Lotto()
'''

# Lotto
'''
class Lotto:
        def __init__(self):
                self.L = range(1,50)
                self.tab=random.sample(self.L,6)
                self.sorted()
        def sorted(self):
                self.tab_sorted=sorted(self.tab)
                #print(self.tab_sorted)
        def __str__(self):
                self.res=''
                for w, v in enumerate(self.tab_sorted):
                        if(w==len(self.tab_sorted) - 1):
                                self.res += str(v)
                        else:
                                self.res+=str(v)+', '
                return 'wyniki ' + self.res
los1=Lotto()
print(los1)
los2=Lotto()
print(los2)
los3=Lotto()
print(los3)
los4=Lotto()
print(los4)
'''

# Dziedziczenie
'''
class szkolenia:
        def __init__(self, nazwa, termin, cena_netto, ilosc_uczestnikow):
                self.nazwa = nazwa
                self.termin = termin
                self.cena_netto = cena_netto
                self.ilosc_uczestnikow = ilosc_uczestnikow
        def obliczKoszt(self):
                self.suma_brutto = (self.cena_netto * ilosc_uczestnikow) * 1.23
                return self.suma_brutto
        
class technologie(szkolenia):
        def __init__(self, nazwa, termin, cena_netto, ilosc_uczestnikow, technologia, poziom):
                super().__init__(nazwa, termin, cena_netto, ilosc_uczestnikow)
                self.technologia = technologia
                self.poziom = poziom

szkolenie1 = technologie('kurs python', '2017-06-30', 200000, 10, 'python', 'podstawowy')
print(szkolenie1.obliczKoszt())
'''
# Dziedziczenie v.2
'''
class szkolenia:
        def __init__(self, nazwa, termin, cena_netto, ilosc_uczestnikow):
                self.nazwa = nazwa
                self.termin = termin
                self.cena_netto = cena_netto
                self.ilosc_uczestnikow = ilosc_uczestnikow
        def obliczKoszt(self):
                self.suma_brutto = (self.cena_netto * self.ilosc_uczestnikow) * 1.23
                return self.suma_brutto

class technologie(szkolenia):
        def __init__(self, nazwa, termin, cena_netto, ilosc_uczestnikow, technologia, poziom):
                super().__init__(nazwa, termin, cena_netto, ilosc_uczestnikow)
                self.technologia = technologia
                self.poziom = poziom
                
class trenerzy(szkolenia):
        def __init__(self, nazwa, termin, cena_netto, ilosc_uczestnikow, technologia, poziom, imie, nazwisko, pensja):
                super().__init__(nazwa, termin, cena_netto, ilosc_uczestnikow)
                self.imie = imie
                self.nazwisko=nazwisko
                self.pensja = pensja
        def obliczKosztTrener(self):
                return self.obliczKoszt() - (self.pensja*1.23)
        

szkolenie1 = technologie('kurs python', '2017-06-30', 200000, 10, 'python', 'podstawowy')
print(szkolenie1.obliczKoszt())
szkolenie2 = trenerzy('kurs python', '2017-06-30', 200000, 10, 'python', 'podstawowy', 'Iks', 'Igrekowski', 2000)
print(szkolenie2.obliczKosztTrener())
'''

#P80
'''
class Produkt:
        def __init__ (self, nazwa, cena):
                self.nazwa = nazwa
                self.cena = cena
        def __str__ (self):
                return 'produkt: ' + self.nazwa + 'cena: ' + str(self.cena)

class Oprogramowanie(Produkt):
        def __init__ (self, nazwa, cena, jezyk, system):
                super().__init__(nazwa, cena)
                self.jezyk = jezyk
                self.system = system
        def __str__ (self):
                return 'produkt: ' + self.nazwa + 'cena: ' + str(self.cena) + ', język: ' + self.jezyk + 'system: ' + self.system

class Szkolenie(Oprogramowanie):
        def __init__(self, nazwa, cena, jezyk, system, termin):
                super().__init__(nazwa, cena, jezyk, system)
                self.termin = termin
        def __str__ (self):
                return 'produkt: ' + self.nazwa + 'cena: ' + str(self.cena) + ', język: ' + self.jezyk + 'system: ' + self.system + 'termin: ' + self.termin

T = Szkolenie('Garncarstwo wysokościowe, ', 1000000, 'pyton 3.99, ', 'Stary Młyn, ', 'jutro')
print(T)
'''

#P80 - RGB
'''
class R:
        def __init__ (self, red):
                self.red = red
        def __str__ (self):
                return 'red (0-255): ' + str(self.red)

class RG(R):
        def __init__ (self, red, green):
                super().__init__(red)
                self.green = green
        def __str__ (self):
                return 'red (0-255): ' + str(self.red) + ', green (0-255): ' + str(self.green) 

class RGB(RG):
        def __init__(self, red, green, blue):
                super().__init__(red, green)
                self.blue = blue
        def __str__ (self):
                        return 'red (0-255): ' + str(self.red) + ', green (0-255): ' + str(self.green) + ', blue (0-255): ' + str(self.blue)
        def __add__ (self, other):
                return 'Twoja Barwa: ['(self.red + other.red)/2, (self.green + other.green)/2, (self.blue + other.blue)/2']'
        
C1 = RGB(0, 20, 30)
print(C1)
C2 = RGB(20, 100, 1)
print(C2)
C3 = C1 + C2
print(C3)
'''
#P80 RGB v.2
'''
class Barwy:
        def __init__ (self, R, G, B):
                self.R = R
                self.G = G
                self.B = B
        def __str__ (self):
                return 'Twoja Barwa: ['+str(self.R)+ ', ' +str(self.G) + ', ' +str(self.B) +']'
        def __add__ (self, other):
                return (self.R + other.R)/2, (self.G + other.G)/2, (self.B + other.B)/2

b1 = Barwy (100, 100, 100)
print(b1)
b2 = Barwy (100, 150, 50)
print(b2)
b3 = b1 + b2
print(b3)
'''

# Pracownik, pensja

class Pracownik:
        def __init__ (self, imie, nazwisko, etat='Staż', pensja=500.000):
                self.imie = imie
                self.nazwisko = nazwisko
                self.etat = etat
                self.pensja = pensja
        def przelicz(self):
                self.pensja_brutto = self.pensja * 1.23
                return self.pensja_brutto, self.pensja
        
class Kontrakt(Pracownik):
        def naKontrakt(self, etat, pensja):
                self.etat = etat
                self.pensja = pensja
        def dodajNadgodziny(self, liczba):
                self.liczba = liczba
                self.pensja = self.pensja + ((self.pensja / (20*8)) * self.liczba)
        def __str__ (self):
                return 'Pensja pracownika ' + self.imie + ' ' + self.nazwisko + ' z nadgodzinami wynosi ' + str(self.pensja * 1.23) + ' zł brutto'

       
p1 = Kontrakt('Tomasz', 'Nałęcz')
print(p1.przelicz())
p1.naKontrakt('Dev', 500)
print(p1.przelicz())
p1.dodajNadgodziny(50)
print(p1.przelicz())
print(p1)

