
from statistics import mean


file=open('forras.txt')
adatsor=file.readlines()

szamok=[]
for elem in adatsor:
    szamok.append(int(elem))

print(szamok)


print(max(szamok))

print(min(szamok))
print(mean(szamok))

maxkul=0
for i in range(len(szamok)-1):
    if maxkul<abs(szamok[i]-szamok[i+1]):
         maxkul=abs(szamok[i]-szamok[i+1])

print(maxkul)