 class Naplo:
    adatsor=[]

    def __init__(self,allomany) -> None:
        bemenet=open(allomany,'r',encoding='UTF-8')
        sorok=bemenet.readlines()
        sorok.remove(sorok[0])
        for sor in sorok:
            bontott=sor.strip('\n').strip('\uffef').split(';')
            self.adatsor.append(
                {
                    'Óra':int(bontott[0]),
                    'Perc':int(bontott[1]),
                    'AdasDb':int(bontott[2]),
                    'Nev':bontott[3]
            
                }
            )
    def kiirNaplo(self):
        print(self.adatsor)

    def bejegyzesSzam(self):
       return (len(self.adatsor))
    
    def percenkent4(self):
        index=0
        while index<len(self.adatsor) and self.adatsor[index]['AdasDb']!=4:
            index+=1
            if index<len(self.adatsor):
                return True
            else:
                return False
    def soforhivasok(self,nev):
     
        osszeg=0
        for elem in self.adatsor:
            if elem['Nev']==nev:
                osszeg+=elem['AdasDb']
            
        return osszeg
    
    def vanSofor(self,nev):
         index=0
         while index<len(self.adatsor) and self.adatsor[index]['Nev']!=nev:
            index+=1
            if index<len(self.adatsor):
                return True
            else:
                return False

    def atvalto(self,ora,perc):
        return ora*60+perc
    
    def ujAllomany(self,allomanyNev):
        with open(allomanyNev,'w',encoding='UTF-8') as f:
            kilista=['Kezdes;Nev;AdasDb\n'] 
            for elem in self.adatsor:
               kilista.append(
                str(self.atvalto(elem['Óra'],elem['Perc']))+';'
               +elem['Nev']+';'+str(elem['AdasDb'])+'\n'
               )
            f.writelines(kilista)
            f.close()
    def becenevek(self):
        bNevek=[]
        for i in range(len(self.adatsor)):
            if bNevek.__contains__(self.adatsor[i]['Nev']):
                i+=1
            else:
                bNevek.append(self.adatsor[i]['Nev'])
            
    

        return len(bNevek)

    def maxhivas(self):
        bNevek=[]
        for a in range(len(self.adatsor)):
            if bNevek.__contains__(self.adatsor[a]['Nev']):
                a+=1
            else:
                bNevek.append(self.adatsor[a]['Nev'])
        hivasok=[]
        for i in range(len(bNevek)):
            osszeshivas=0
            for j in range(len(self.adatsor)):
                if bNevek[i]==self.adatsor[j]['Nev']:
                    osszeshivas+=self.adatsor[j]['AdasDb']
            hivasok.append(osszeshivas)
        nev=''
        for d in range(len(hivasok)):
            if hivasok[d]==max(hivasok):
                nev=bNevek[d]

        
        print(f'9. feladat: Legtöbb adást indító sofőr\n\tNév: {nev}\n\tAdások száma: {max(hivasok)} alkalom')

            
            





ujjnaplo=Naplo('cb.txt')
print(f'3. feladat: Bejegyzések száma: {ujjnaplo.bejegyzesSzam()} db')
if ujjnaplo.percenkent4():
    print('4. feladat: Volt négy adást indító sofőr')
else:
    print('Nem volt négy adást indító sofőr')

nev=input('5. feladat: Kérek egy nevet ')
if not ujjnaplo.vanSofor(nev):
    print(f'\t{nev} {str(ujjnaplo.soforhivasok(nev))}x használta a CB-rádiót')
else:
     print('\tNincs ilyen nevű sofőr')

print('Összperc: ',str(ujjnaplo.atvalto(ujjnaplo.adatsor[0]['Óra'],ujjnaplo.adatsor[0]['Perc'])))

print(f'8. feladat: Sofőrök száma: {ujjnaplo.becenevek()}')


ujjnaplo.maxhivas()
allomanyNev="cb2.txt"
ujjnaplo.ujAllomany(allomanyNev)

