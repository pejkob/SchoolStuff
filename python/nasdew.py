
szam=int(input('Adjon meg egy számot! '))
darabszam=0
while True:
   
   if szam>0:
    darabszam+=1
    szam=int(input('Adjon meg egy számot! '))
    if szam<0:
        darabszam+=1
        szam=int(input('Adjon meg egy számot! '))
   if szam==0:
    darabszam+=1
    szam=int(input('Adjon meg egy számot! '))

   else:
    print(darabszam)
    break
    
