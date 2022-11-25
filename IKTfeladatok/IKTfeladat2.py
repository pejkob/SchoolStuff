szoveg=input('Adjon meg egy szöveget! ')
szam=int(input('Adjon meg egy egész számot! '))

betuk=[]
for betu in szoveg:
    betuk.append(betu)

eleje=''
vege=''
for i in range(len(betuk)):
    if i<szam:
        eleje+=betuk[i]
    else:
        vege+=betuk[i]


print(vege+eleje)