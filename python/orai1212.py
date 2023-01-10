#egy boltban a vásárlónak bizalompontok után kedvezményt adnak 100 pont és 200 pont között 2% kedvezmény jár 200 pont fölött 4% kedvezmény jár, készítsen függvényt amelynek két paramétere
# van az egyik az ár a másik a kedvezményes érték 
import random
def kedvezmennyel(ar,pontok):
    if pontok>=100 and pontok<=200:
        return ar-(ar*0.02)
    if pontok>200:
        return ar-(ar*0.04)

#a vásárlói kosárban 12 termék ára található kérje be a felhasználótól bizalompontjainak számát és írja ki a fizetendő összeget
termekarak=[1500,700,480,230,250,540,875,1800,1500,1210,150,1230]
pontok=int(input('Adja meg bizalompontjainak számát! '))

for i in range(len(termekarak)):
    print(f'Fizetendő: {round(kedvezmennyel(termekarak[i],pontok))} Ft')



#kosar.txt-ben 8 termék megnevezés;ár
with open('kosar.txt','w',encoding='utf-8') as w:
    w.writelines('banán'+';'+'1500'+'\n'+'alma'+';'+'500'+'\n'+'körte'+';'+'400'+'\n'+'szilva'+';'+'500'+'\n'+'meggy'+';'+'700'+'\n'+'cseresznye'+';'+'1200'+'\n'+'narancs'+';'+'24500'+'\n'+'tök'+';'+'11500'+'\n')

#kérdezzen rá a program hogy szeretne e másik kosárból beolvasni, kérje be a bizalompontok számát és számítsa ki a kedvezményeket

answer=input('Szeretné a kosárban lévő termékekre is alkalmazni a kedvezményeket? (y/n)')
kedvezmenyesar=[]
if answer.lower()=='y':
    with open('kosar.txt','r',encoding='utf-8') as f:
        sorok=f.readlines()
        for sor in sorok:
            termek=sor.split(';')[0]
            ar=int(sor.split(';')[1])
            kedvezmenyesar.append({termek:round(kedvezmennyel(ar,pontok))})
          

#írja ki a fizetendo.txt-be a termékek megnevezését utána pontosvesszővel elválasztva a ténylegesen fizetendő árat és az utolsó sorban az összesen fizetendő árat

with open('fizetendo.txt','w',encoding='utf-8') as w2:
    w2.writelines(str(kedvezmenyesar)+'\n')

rndadatok=[]
for i in range(12):
    rnd=random.randint(1,400)
    rndadatok.append(rnd)

for i in range(len(termekarak)):
    print(f'asd: {kedvezmennyel(termekarak[i],pontok)}')