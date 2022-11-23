class ultrabalaton:
    adatok=[]
    def __init__(self,allomanynev) -> None:
            f=open(allomanynev,'r',encoding='utf-8')
            sorok=f.readlines()
            sorok.remove(sorok[0])
            for sor in sorok:
                bontott=sor.strip('\n').split(';')
                self.adatok.append(
                    {
                    'Versenyző':bontott[0],
                    'Rajtszam':int(bontott[1]),
                    'Kategoria':bontott[2],
                    'Versenyido':bontott[3],
                    'VersenyO':int(bontott[3].split(':')[0]),
                    'VersenyP':int(bontott[3].split(':')[1]),
                    'VersenyMP':int(bontott[3].split(':')[2]),
                    'TavSzazalek':int(bontott[4])
                }
                )
    def kiir(self):
        print(self.adatok)
    
    def feladat1(self):
        return len(self.adatok)
    
    def feladat2(self):
        noiVersenyzok=0
        for elem in self.adatok:
            if elem['Kategoria']=="Noi" and elem['TavSzazalek']==100:
                noiVersenyzok+=1
        return noiVersenyzok
    
    def feladat3(self,sportolo):
       versenyzik=False
       teljesitett=False
       for elem in self.adatok:
        if elem['Versenyző']==sportolo:
            versenyzik=True
            if elem['TavSzazalek']==100:
                teljesitett=True
       if versenyzik:
            print(f'\tIndult egyéniben a sportoló? Igen')
            if teljesitett:
                 print(f'\tTeljesítette a távot? Igen')
            else:print(f'\tIndult egyéniben a sportoló? Nem')
      
       else:print(f'\tTeljesítette a távot? Nem')
    
    def IdőÓrában(self,i):
        ora=self.adatok[i]['VersenyO']
        perc=self.adatok[i]['VersenyP']
        mperc=self.adatok[i]['VersenyMP']
        return ora+perc/60+mperc/3600
    def atlag(self):
        sum=0
        db=0
        for i in range(len(self.adatok)):
            if self.adatok[i]['Kategoria']=='Ferfi' and self.adatok[i]['TavSzazalek']==100:
                sum+=self.feladlsad(i)
                db+=1
        print(f'7. feladat: Átlagos idő: {sum/db} óra')
        
        #8.feladat
    
   

file=ultrabalaton('ub2017egyeni.txt')

print(f'3. feladat: Egyéni indulók: {file.feladat1()} fő')

print(f'4. feladat: Célba érkező női sportolók: {file.feladat2()} fő')

sportolo=input('5. feladat: Kérem a sporoló nevét ')
file.feladat3(sportolo)
file.atlag()
