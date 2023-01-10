file=open('furdoadat.txt','rt',encoding='UTF-8')
sorok=file.readlines()

adatok=[]
for i in range(len(sorok)):
    ujsor={}
    ujsor['vendegid']=int(sorok[i].split(' ')[0])
    ujsor['furdoid']=int(sorok[i].split(' ')[1])
    ujsor['beki']=int(sorok[i].split(' ')[2])
    ujsor['hour']=int(sorok[i].split(' ')[3])
    ujsor['min']=int(sorok[i].split(' ')[4])
    ujsor['sec']=int(sorok[i].split(' ')[5])
    adatok.append(ujsor)

print(sorok)