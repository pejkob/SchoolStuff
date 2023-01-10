import szoveges
file=open('epertorta.txt','rt',encoding='UTF-8')
sorok=file.readlines()

adatok=[]
for elem in sorok:

    adatok.append(elem.strip('\n'))

reszlet='és'
print(szoveges.szoValogato(adatok,reszlet))
szodb='t'
print(szoveges.szoDarab(adatok,szodb))
with open('valogatas.txt','w',encoding='UTF-8') as w:
    w.write(str(szoveges.szoValogato(adatok,reszlet)))
    

    