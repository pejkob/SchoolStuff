szoveg=input('Adjon meg egy szöveget! ')
betuk=['a','á','b','c','d','e','é','f','g','h','i','í','j','k','l','m','n','o','ó','ö','ő','p','q','r','s','t','u','ú','ü','ű','v','w','x','y','z']
szamok=['0','1','2','3','4','5','6','7','8','9']
letter=0
digit=0
other=0

for char in szoveg:
    if char in betuk:
        letter+=1
    elif char in szamok:
        digit+=1
    else:
        other+=1

print(f'A szövegben van {letter} betű, {digit} szám és {other} egyéb karakter')
