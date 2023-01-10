from itertools import count


file=open('utasadat.txt','rt',encoding='UTF-8')
lines=file.readlines()

data=[]

for i in lines:
    newline=i.strip('\n').split()
    line={
        'sorszam':int(newline[0]),
        'datum':newline[1],
        'azonosito':int(newline[2]),
        'tipus':newline[3],
        'ervenyesseg':int(newline[4])

    }
    data.append(line)

numb=0
for line in data:
    numb+=1

print('2.feladat')
print('A buszra',numb,'utas akart felszállni.')

denied=0
for line in data:
    if line['tipus'] == 'JGY' and line['ervenyesseg'] == 0 or line['tipus'] != 'JGY' and line['ervenyesseg']<int(line['datum'].split('-')[0]):
        denied+=1

print('3.feladat')
print('A buszra',denied,'utas nem szállhatott fel.')
        

print('4.feladat')
countId={
}

for line in data:
    if str(line['sorszam']) in countId:
        countId[str(line['sorszam'])]+=1
    else:
        countId[str(line['sorszam'])]=1

print(countId)
print(max(countId))
print(max(countId,key=countId.get))
        

    
