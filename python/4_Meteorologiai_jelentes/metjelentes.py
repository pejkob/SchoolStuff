file=open('tavirathu13.txt','r',encoding='UTF-8')
sorok=file.readlines()
adatok=[]

for sor in sorok:
    splitted=sor.strip('\n').split(' ')
    diction={}
    diction['Település']=splitted[0]
    diction['Idő']=splitted[1]
    diction['Irány']=splitted[2]
    diction['Hőmérséklet']=splitted[3]
    adatok.append(diction)

feladat1=input('Adja meg a település kódját ')

index=len(adatok)-1
while adatok[index]['Település']!=feladat1:
    index-=1

print(f"Az utolsó mérési adat a megadott telephelyről: {adatok[index]['Idő'][0:2]}:{adatok[index]['Idő'][2:4]} -kor érkezett ")

maxadat=0
minadat=33
maxidoido=20
minido=20
for elem in adatok:
    if int(elem['Hőmérséklet'])>maxadat:
        maxadat=int(elem['Hőmérséklet'])
        ido=int(elem['Idő']) 
    if int(elem['Hőmérséklet'])<minadat:
        minadat=int(elem['Hőmérséklet'])
        minido=int(elem['Idő'])

print(f'Minimum hőmérséklet:{minadat} Ekkor: {minido}\nMaximum hőmérséklet:{maxadat} Ekkor:{maxidoido} ')

