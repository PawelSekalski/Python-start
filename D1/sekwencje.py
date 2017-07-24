# -*- coding: utf-8 -*-

'''
napis = "uwaga! oto jest długi napis"
napis[3] = 't'
print(napis)
'''

'''
# duża litera
napis = "zaznaczenie sszaznass"
print(napis.capitalize())

# liczenie znaków
print(napis.count("z"))

# 
print(napis.islower())

#
print(napis.index("z"))

#
print(napis.isspace())

#
print(napis.replace("zazna","owa"))
'''

'''
# deklarowanie list, indeksowanie od zera!!!!!!

lista = []
lista.append(1)
lista.append('abc')
lista.append('Q')
lista.append("asdfg")

print(lista[0], lista[1], lista[2])
print(lista[3])
'''

'''
# deklaracja i przypisanie wartości
oceny = []
a = (input("podaj ocenę: "))
oceny.append(a)
oceny.append(input("podaj drugą ocenę: "))
print(oceny[0], oceny[1])
oceny[0] = '5'
print(oceny[0], oceny[1])
'''

'''
# wykazanie poszczególnych ocen w liście

oceny2 = [3,4,5]
print(oceny2[0])
print(oceny2[1])
print(oceny2[2])
'''

'''
# lista w liście

listlist = [2, 3, 4], ['a', ['robbraider', 2, 'klm'], 'c']
print(listlist[1][1][0])
'''

'''
# odwołanie przedział, indeks start, stop

oceny = [3,4,5,6,6,7,8,9,10]
print(oceny[2:6])

# co druga pozycja [start::co ile]

oceny = [3,4,5,5,6,7,8,9,10]
print(oceny[1::2])

# ile pozycji

oceny = [3,4,5,6,7,8,9,10]
print(len(oceny))
'''

'''
# konwersja napisu na listę (literowanie)

tekst = "napis"
lista = list(tekst)
print(lista)
# podmianka pozycji

lista[2] = 'w'
print(lista)

# usuwanie pozycji pop'em

lista.pop(2)
print(lista)

lista[2] = 'w'
print(lista)
print(len(lista))
'''

'''
# lista zestawienie !!!!poprawić!!!!
art = [["cukier", "smalec", "ocet"],[1.99, 4, 5.45]]
suma = (art[1][0] + art[1][1] + art[1][2])
print("nazwa\t\tcena")
print("_______\t\t_______")
print(art[0][0] + '\t\t' + str(art[1][0]))
print(art[0][1] + '\t\t' + str(art[1][1]))
print(art[0][2] + '\t\t' + str(art[1][2]))
print(round(suma))
'''

'''
# typy skwerencyjne - krotki

data = (("cukier", "smalec", "ocet"),('14-10-1991', '01-09-1999', '22-12-2007'))
print(data)
print("nazwa\t\tdata")
print(data[0][0] + '\t\t' + str(data[1][0]))
print(data[0][1] + '\t\t' + str(data[1][1]))
print(data[0][2] + '\t\t' + str(data[1][2]))
'''

tabela = [("Dżoana", "Paszczak", "Brajanek"),('14-10-2009', '01-09-2001', '22-12-2007'),['nic', 'zero', 'mięso armatnie']]
# zmiana w tabeli, która przejdzie: tabela[2][0] = 'szef'
# zmiana w krotce, która nie przejdzie: tabela[0][1] = 'Mariusz'
print('imię' + '\t\t' + 'data urodzenia' + '\t' + 'stanowisko')
print('___________' + '\t' + '___________' + '\t' + '___________')
print(tabela[0][0] + '\t\t' + str(tabela[1][0]) + '\t' + tabela[2][0])
print(tabela[0][1] + '\t' + str(tabela[1][1]) + '\t' + tabela[2][1])
print(tabela[0][2] + '\t' + str(tabela[1][2]) + '\t' + tabela[2][2])
