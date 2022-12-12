szam1=float(input('Kérem, adjon meg az első valós számot: '))
szam2=float(input('Kérem, adja meg a második valós számot: '))
szam3=float(input('Kérem, adja meg a harmadik valós számot: '))

maxszam=0
if szam1>szam2 and szam1>szam3:
    maxszam=szam1
    if szam2+szam3==0:
        print('Nem lehet osztani')
    else:
        print(f'A kért hányados: {maxszam/(szam2+szam3)}')

if szam2>szam1 and szam2>szam3:
    maxszam=szam2
    if szam2+szam3==0:
        print('Nem lehet osztani')
    else:
        print(f'A kért hányados: {maxszam/(szam1+szam3)}')

if szam3>szam1 and szam3>szam2:
    maxszam=szam3
    if szam2+szam3==0:
        print('Nem lehet osztani')
    else:
        print(f'A kért hányados: {maxszam/(szam1+szam2)}')

