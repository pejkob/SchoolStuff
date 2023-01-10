import random
#1.feladat
num1=int(input('Adja meg az első számot! '))
num2=int(input('Adja meg a második számot! '))
while abs(num1-num2)!=15:
    num1=int(input('Adja meg az első számot! '))
    num2=int(input('Adja meg a második számot! '))
print(f'A különbség a {num1} és a {num2} között: {abs(num1-num2)}')

#2.feladat

betuk="abcdefghijklmnopqrstouvwxyzABCDEFGHIJKLMNOPQRSTOUVWXYZ123456789"
szoveg=[]
for i in range(30):
    rnd=random.randint(0,len(betuk)-1)
    szoveg.append(betuk[rnd])

for betu in szoveg:
    print(betu,end='')

print()

for i in range(1,len(szoveg)):
    if i%5==0:
        print(szoveg[i],end=',')


#3.feladat

adatok={
    'Családnév':'Pejkó',
    'Keresztnév':'Bálint',
    'Születési hely':'Miskolc',
    'Születési év':int(2004)
}
print()
nev1=input('Adja meg a családnevét')
nev2=input('Adja meg a keresztnevét')
szhely=input('Adja meg a születési helyét')
szev=int(input('Adja meg születési évét'))

newadatok={
    'Családnév':nev1,
    'Keresztnév':nev2,
    'Születési hely':szhely,
    'Születési év':szev
}
print(newadatok)

#4.feladat
file=open('forras.txt','rt',encoding='UTF-8')
sorok=file.readlines()

tomb=[]
for i in range(len(sorok)):
    lines={}
    lines['Település neve:']=sorok[i].split(';')[0]
    lines['Megye:']=sorok[i].split(';')[1]
    lines['Népesség']=int(sorok[i].split(';')[2])

