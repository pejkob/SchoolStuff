import random
def feladat1():
    tomb=[]
    for i in range(17):
        rnd=random.randint(3,52)
        tomb.append(rnd)
    print(f'Tömb max eleme: {max(tomb)}\nTömb min eleme: {min(tomb)}')
    
def feladat2():
    tomb2=[]
    index=5
    rnd=random.randint(0,5)
    for i in range(5):
        tomb2.append(input(f'Adjon meg egy nevet! {index} '))
        index-=1
    
    print(f'A tömb egyik eleme: {tomb2[rnd]} Az elem hossza: {len(tomb2[rnd])}')

def feladat3():
    tomb3=[]
    rnd=random.randint(50,60)
    for i in range(rnd):
        tomb3.append(12)
    
    print(tomb3)
    print(len(tomb3))

def feladat4():
    szoveg=input('Adjon meg egy szöveget ')
    while len(szoveg)<=10:
        print('Nem megfelelő karakterszám')
        szoveg=input('Adjon meg egy szöveget ')
        

def feladat5():
    szo=input('Adjon meg egy szót ')
    ekezetek='áéőúűóüö'
    van=False
    for betu in szo:
        if ekezetek.__contains__(betu):
            van=True

    if van:
        print('Van benne magyar ékezetes betű!')
    else:
        print('Nincs benne magyar ékezetes betű!')    


def feladat6():
    szoveg=input('Adjon meg egy szöveget! ')
    ecount=0
    for betu in szoveg:
        if betu=='e':
            ecount+=1
    print(f'Ennyi e betű van a szövegben: {ecount}')


def feladat7():
     szoveg=input('Adjon meg egy szöveget! ')
     for i in range(len(szoveg)):
        if i%2==1:
            print(szoveg[i])

def feladat8():
     szoveg=input('Adjon meg egy szöveget! ')
     s=szoveg.split()
     szohossz=[]
     for i in range(len(s)):
            szohossz.append(len(s[i]))
     print(f'A szövegben a szavak {szohossz} hosszúak')    

def feladat9():
     szoveg=input('Adjon meg egy szöveget! ')
     s=szoveg.split()
     rnd=random.randint(0,len(s)-1)
     print(s[rnd])

def feladat10():
    tomb4=[]
    for i in range(20):
        rnd=random.randint(5,65)
        tomb4.append(rnd)
    rndnum1=random.randint(0,len(tomb4))
    rndnum2=random.randint(0,len(tomb4))
    print(tomb4)
    print(rndnum1+rndnum2)

def feladat11():
    a=random.randint(10,31)
    b=random.randint(10,31)
    c=random.randint(10,31)
    if a+b>c and b+c>a and a+c>b:
        print(f'Az alábbi adatokkal a háromszög megszerkeszthető {a} {b} {c}')
    else: print('A háromszög nem megszerkeszthető')

def feladat12():
    szam=int(input('Adjon meg egy számot '))
    szam2=szam
    rev = 0
    while(szam2>0):
        a=szam2%10
        rev=rev*10+a
        szam2=szam2//10
    
    print(f'Eredmény:{szam-rev}')

def feladat13():
    szoveg=input('Adjon meg 3 szót! ')
    s=szoveg.split()
    maxelem=0
    for elem in s:
        if len(elem)>maxelem:
            maxelem=elem
    print(maxelem)





   

feladat13()   

