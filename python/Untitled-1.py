''' 1.Feladat : egy boltban a vásárlónak bizalompontok után kedvezményt adnak 100-200 pont között 2%kedvezmény, 200 pont felett 4%kedvezmény jár, készítsen egy függvényt amelynek két paramétere van, az egyik az ár, a másik a pontok száma, visszatérési értéke a változott ár ''' 

from math import floor
import random


def Kedvezmennyel(ar,pontszam):
    valtozottar = 0
    if pontszam >= 100 and pontszam <= 200:
        valtozottar +=float(ar*0.98)
    elif pontszam > 200 :
        valtozottar += float(ar*0.96)
    return valtozottar

'''A vásárlói kosárban 12 termék ára található, kérje be a felhasználótól bizalompontjainak számát és írja ki a fizetendő összeget'''
print(Kedvezmennyel(500,150))
pontok=int(input('odsgfoi,: '))
rndadatok=[]
for i in range(12):
    rnd=random.randint(1,400)
    rndadatok.append(rnd)

for i in range(len(rndadatok)):
    print(f'asd: {Kedvezmennyel(rndadatok[i],pontok)}')

termekek = []

with open('kosar.txt','r',encoding="UTF-8") as o:
    lines = o.readlines()

    for item in lines :
        splitted = item.split(';')
        termekek.append({
            'Terméknév' : splitted[0],
            'Árak' : splitted[1]
        })

for item in termekek :
    print(f'A kosár tartalma kedvezményesen : {item["Terméknév"]} {Kedvezmennyel(item["Árak"],pontok)}')
