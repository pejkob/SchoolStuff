import imp
from lib2to3.pgen2.literals import evalString
from operator import truediv
from turtle import clear
import random


print('1')
szam = int(input('Adj meg egy számot! '))
szam1=int(input('Adjon meg egy másik számot'))
if szam < szam1:
      print("csökkenő sorrend")
      print(szam1)
      print(szam)
else:
      print("csökkenő sorrend")
      print(szam)
      print(szam1)

var1= int(input('Adj meg egy számot! '))
var2 = int(input('Adj meg egy számot! '))
var3 = int(input('Adj meg egy számot! '))
lista=[var1,var2,var3]
max=lista[0]

for szam in lista:
	if szam > max:
		max = szam

print('A legnagyobb szám: ',max)
input('Press Enter to continue')
clear
print('2')

rand=random.randint(9,100)
talalat=False
bekertszam=int(input('random szám'))
while not talalat:
    if bekertszam!=rand:
        if bekertszam>rand:
            print('A szám kisebb')
            bekertszam=int(input('random szám'))
        else:
            print('A szám nagyobb')
            bekertszam=int(input('random szám'))

    else:
        talalat=True
        print('Találat')        

input('Press Enter to continue')
clear
print('3')




lst = []

for i in range(0,5):
    rand1=random.randint(10,20)
    lst.append(rand1)


print(lst)
