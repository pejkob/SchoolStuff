file=open('termes.csv')
sor=file.readlines()

fejlec=sor[0].strip().split(';')
print(fejlec)
tablazat=[]

for i in range(1,len(sor)):
    bontott=sor[i].strip().split(';')
    szamsor=[]
    for j in range(len(bontott)):
        szamsor.append(int(bontott[j]))
    
    tablazat.append(szamsor)

for fajta in range(1,len(fejlec)):
    maxtermes=0
    for i in range(len(tablazat)):
        if tablazat[maxtermes][fajta]<tablazat[i][fajta]:
            maxtermes=i
    print('A(z)',fejlec[fajta],'legnagyobb termése',tablazat[maxtermes][0],'évben volt')