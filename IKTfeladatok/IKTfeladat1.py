szoveg=input('Adjon meg egy szöveget! ')
szam=int(input('Adjon meg egy egész számot! '))

if szam<len(szoveg) and szam>0:
    print(szoveg[szam-1])
else:
    print('Nem létező karakter!')