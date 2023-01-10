from lib2to3.pytree import convert
from tokenize import Number

#Alap verzió
elsoszam=int(input('Adja meg a számtani sorozat első tagját'))
diff=int(input('Adja meg mekkora legyen a differencia'))
szamdb=int(input('Adja meg hány számot szeretne kiíratni a sorozatból'))
sorozat=[]
sorozat.append(elsoszam)
index=0

while index<szamdb-1:
    sorozatelem=sorozat[index]+diff
    sorozat.append(sorozatelem)
    index+=1

print(sorozat)
#Fejlesztett verzió

felsoszam=int(input('Adja meg a számtani sorozat első tagját'))
fdiff=int(input('Adja meg mekkora legyen a differencia'))
fszamdb=int(input('Adja meg hány számot szeretne kiíratni a sorozatból'))
elsokiirando=int(input('Hanyadik tagot írjuk ki először?'))
fsorozat=[]
fsorozat.append(felsoszam)
for i in range(elsokiirando-1,elsokiirando+fszamdb-1):
   
    print(felsoszam+fdiff*1, end=',')


