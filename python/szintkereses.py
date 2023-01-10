darab=0
szo=""
darab=int(input('Adjon meg egy számot '))
szo=input('Adjon meg egy szot ')
#print(len(szo))

#if darab%3==0:
#    print('3-mal osztható számot kaptam')


szamok1=[0,0,0,0,0,0]
szamok2=[]
szamok3=[2,7,21,33,20,9]
print(szamok1)
print(szamok2)

for i in range(darab):
    szamok2.append(0)

for i in range(len(szamok3)):
    print(f'{szamok3[i]}',end=' ')

print(' ')
#for i in range(len(szamok1)):
 #   szamok1[i]=input('Az első tömb elemei ')

print(szamok1)

import random

for i in range(len(szamok2)):
    
    szamok2[i]=random.randint(25,51)

print(szamok2)

if szo.__contains__('e'):
    print('Van e betű a szóban')
else:print('Nincs e betű a szóban')
szamok2osszege=0
for i in range(len(szamok2)):
    
    szamok2osszege+=szamok2[i]

print(szamok2osszege)

szocount=0
#szoveg=input('Adjon meg egy szöveget')
#szocount=len(szoveg.split(' '))

#print(f'{szocount} szó van a szövegben')

paratlan=[]
paratlanindex=[]
for i in range(len(szamok2)):
    if szamok2[i]%2==1:
        paratlan.append(szamok2[i])
        paratlanindex.append(i)
   
print(paratlan)
print(paratlanindex)    


for i in range(len(szo)):
    if i%3==0:
        print(szo[i],end=' ')


for i in range(len(szamok3)):
    if szamok3[i]<len(szo):
        print(szamok3[i])