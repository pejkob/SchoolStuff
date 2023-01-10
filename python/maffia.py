from base64 import encode

file=open('adatok.csv','rt',encoding='UTF-8')
sorok=file.readlines()
fejlec=sorok[0].strip('\ufeff').strip('\n').split(';')
adatok=[]

for i in range(1,len(sorok)):
    ujsor=[]
    ujsor.append(sorok[i].split(';')[0])
    ujsor.append(int(sorok[i].split(';')[1]))
    ujsor.append(sorok[i].split(';')[2])
    ujsor.append(int(sorok[i].split(';')[3]))
    adatok.append(ujsor)

legidosebb=0

for i in range(len(adatok)):
    if adatok[legidosebb][1]>adatok[i][1]:
        legidosebb=i

legfiatalabb=0
for i in range(len(adatok)):
    if adatok[legfiatalabb][1]<adatok[i][1]:
        legfiatalabb=i


leggyengebb=0
for i in range(len(adatok)):
    if adatok[leggyengebb][3]>adatok[i][3]:
      leggyengebb=i

str1='A legidősebb ember:',adatok[legidosebb][0] 
str2='A legfiatalabb ember ennyi jövedelmet termelt',adatok[legfiatalabb][3],'Ft'
str3='A maffiózó',adatok[leggyengebb][2],'-ba fog utazni'
r=open('jelentes.txt', 'w', encoding='UTF-8')
r.write(str(str1))
r.write(str(str2))
r.write(str(str3))

r.close
print('Fájlba írás kész')


