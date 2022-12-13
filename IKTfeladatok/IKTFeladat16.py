szoveg=input('Adjon meg egyszöveget')

eredmeny=0
for betu in szoveg:
    if betu.isdigit():
        eredmeny=eredmeny+int(betu)


print(eredmeny)
