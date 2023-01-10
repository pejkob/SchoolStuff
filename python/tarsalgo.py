




def idotartam(beOra,bePerc,kiOra,kiPerc):
    return (kiOra*60+kiPerc)-(beOra*60+bePerc)


file=open('ajto.txt','rt',encoding='UTF-8')
sorok=file.readlines()

adatok=[]
for elem in sorok:
    bontottSor=elem.strip('\n').split(' ')
    ujsor={
        'ora':int(bontottSor[0]),
        'perc':int(bontottSor[1]),
        'azon':int(bontottSor[2]),
        'beki':bontottSor[3]
    }
    adatok.append(ujsor)
    
szam=0
for elem in adatok:
    if elem['beki']=='be':
        szam+= 1
    else:
        szam-=1    

szemelyek={}    
for elem in adatok:
    if str(elem['azon']) in szemelyek:
        if elem['beki']=='be':
            szemelyek[str(elem['azon'])]+=1
        else:
            szemelyek[str(elem['azon'])]-=1
    else:
        szemelyek[str(elem['azon'])]=1
emberek=[]
for ember in szemelyek:
    if szemelyek[ember]==1:
        emberek.append(ember)

emberek.sort()
print(emberek)

aktualisletszam=0
maxletszam=0
maxhelye=0
for i in range(len(adatok)):
    
    if adatok[i]['beki']=='be':
        aktualisletszam+=1
        if aktualisletszam>maxletszam:
            maxletszam=aktualisletszam
            maxhelye=i
    else: aktualisletszam-=1


print('A maximális létszám: ',maxletszam,' Ideje:',adatok[maxhelye]['ora'],':',adatok[maxhelye]['perc'])    

bemenet=int(input('Adja meg a személy azonosítóját! '))
bentTartozkodott=0
for i in adatok:
    if i['azon']==bemenet:
        if i['beki']=='be':
            print(i['ora'],end=':')
            print(i['perc'],end='-')
            belepesOra=i['ora']
            belepesPerc=i['perc']
            bentvan=True
        elif i['beki']=='ki':
            print(i['ora'],end=':')
            print(i['perc'])
            bentTartozkodott+=idotartam(belepesOra,belepesPerc,i['ora'],i['perc'])
            bentvan=False
        
print('\n',bentTartozkodott)
            
