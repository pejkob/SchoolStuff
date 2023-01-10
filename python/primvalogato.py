import pintool

bemenet=open('kimenet.txt','r',encoding='UTF-8')
szamok=bemenet.readlines()
szamsorok=[]
for i in szamok:
    szamsorok.append(int(i))
print(szamsorok)

index=0
while index<len(szamsorok) and not pintool.prim_e(szamsorok[index]):
    index+=1
if index<len(szamsorok):
    print('Van benne prímszám')
else:
    print('Nincs benne prímszám')

primcount=0
for i in range(len(szamsorok)):
    if pintool.prim_e(szamsorok[i])==True:
        primcount+=1

print(f'Prímszámok:{primcount}\nNem prímszámok:{len(szamsorok)-primcount}')