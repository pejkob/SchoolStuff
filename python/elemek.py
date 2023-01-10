class wikipedia:
    adatsor=[]
    def __init__(self,allomaynev) -> None:
        with open(allomaynev,'r',encoding='UTF-8') as f:
            sorok=f.readlines()
            for sor in sorok:
                splitelt=sor.strip('\ufeff').split(';')

                self.adatsor.append({
                    'Rendszám':int(splitelt[0]),
                    'Vegyjel':splitelt[1],
                    'Név':splitelt[2],
                    'Atomtömeg':float(splitelt[3]),
                    'Sűrűség':float(splitelt[4]),
                    'Olvadáspont':float(splitelt[5]),
                    'Forráspont':float(splitelt[6]),
                    'Fajhő':float(splitelt[7]),
                    'Elektronegativitás':float(splitelt[8])
                })
    def kiir(self):
        print(self.adatsor)
    
    def feladat2(self,rendszam):
        print('\nFeladat2')
        van=False
        Vegyjel=''
        Nev=''
        Atom=0
        for sor in self.adatsor:
            if sor['Rendszám']==rendszam:
                van=True
                Vegyjel=sor['Vegyjel']
                Nev=sor['Név']
                Atom=sor['Atomtömeg']
                
        if van:
            print(Vegyjel,Nev,Atom)
        else:print('HIÁNYZIK')

    def feladat3(self):
        print('\nFeladat3')
        for sor in self.adatsor:
            nev=sor['Név']
            vegyjel=sor['Vegyjel'].lower()
            if nev.startswith(vegyjel):
               print(nev,end=', ')

    def feladat4(self):
       print('\nFeladat4')
       szobaH=293
       for sor in self.adatsor:
        if sor['Olvadáspont']<szobaH and sor['Forráspont']>szobaH and sor['Olvadáspont']!=0:
            print(sor['Név'],sor['Olvadáspont'],sor['Forráspont'])
        #olvadáspont alacsonabb  fagyáspont magasabb
    def feladat5(self):
        print('\nFeladat5')
        maxSuruseg=self.adatsor[0]['Sűrűség']
        maxElem=''

        for sor in self.adatsor:
            if sor['Sűrűség']>maxSuruseg:
                maxSuruseg=sor['Sűrűség']
                maxElem=sor['Rendszám']
        print(maxElem,maxSuruseg)
    def feladat6(self):
        print('\nFeladat6')
        for sor in self.adatsor:
            if sor['Elektronegativitás']>4:
                return True
    def feladat7(self):
        tomeg=0
        rendszam=0
        neutronSzamok=[]
        for sor in self.adatsor:
            tomeg=round(sor['Atomtömeg'])
            rendszam=sor['Rendszám']
            if sor['Atomtömeg']==0:
                neutronSzamok.append(-1)
            
            neutronszam=tomeg-rendszam
            neutronSzamok.append(neutronszam)
    def feladat8(self):
        szobaH=293
        #elem forráspontja alacsonabb mint a szobaH
        gazok=[]
        for sor in self.adatsor:
            if sor['Forráspont']<szobaH:
                gazok.append(sor['Név']+'\n')
        
        with open('gaz.txt','w',encoding='UTF-8') as w:
            w.writelines(gazok)

           

            




wiki=wikipedia('kemiai.csv')

rendszam=int(input('Adjon meg egy rendszámot! '))
wiki.feladat2(rendszam)
wiki.feladat3()
wiki.feladat4()
wiki.feladat5()
if wiki.feladat6():
    print('Van')
else:
    print('Nincs')

wiki.feladat8()