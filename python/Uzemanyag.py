import math
class Uzemanyag:
    adatok=[]
    def __init__(self,allomanynev) -> None:
        with open(allomanynev,'r',encoding='UTF-8') as f:
            sorok=f.readlines()
            for sor in sorok:
                reszlet=sor.strip('\n').split(';')
                self.adatok.append(
                    {
                        'Datum':reszlet[0],
                        'Ev':int(reszlet[0].split('.')[0]),
                        'Honap':int(reszlet[0].split('.')[1]),
                        'Nap':int(reszlet[0].split('.')[2]),
                        'Benzin':int(reszlet[1]),
                        'Gazolaj':int(reszlet[2])
                    }
                )
    def feladat2(self):
        print(self.adatok)
    def feladat3(self):
        print(f'3. feladat: Változások száma: {len(self.adatok)}')
    def feladat4(self):
        kulonbseg=[]
        for elem in self.adatok:
            benzin=elem['Benzin']
            gazolaj=elem['Gazolaj']
            kulonbseg.append(abs(benzin-gazolaj))
        print(f'4. feladat: A legkisebb különbség: {min(kulonbseg)}')
    def feladat5(self):
        legkisebb=[]
        
        for elem in self.adatok:
            benzin=elem['Benzin']
            gazolaj=elem['Gazolaj']
            if abs(benzin-gazolaj)==0:
                legkisebb.append(abs(benzin-gazolaj))
        print(f'5. feladat: A legkisebb különbség előfordulása: {len(legkisebb)}')
    
    def feladat6(self):
        for elem in self.adatok:
            if elem['Ev']%4==0 and elem['Nap']==24 and elem['Honap']==2:
                print(f'6. feladat: Volt változás szökőnapon!')
                

    def feladat7(self):
        with open('euro.txt','w',encoding='UTF-8') as w:
            arfolyam=307.7
            
            for elem in self.adatok:
                gazar=round(elem['Gazolaj']/arfolyam,2)
                olajar=round(elem['Benzin']/arfolyam,2)
                w.writelines(elem['Datum']+';'+str(olajar)+';'+str(gazar)+'\n')
    def feladat8(self):
        evszam=int(input('8. feladat: Kérem adja meg az évszámot [2011..2016]: '))
        while 2011>=evszam or evszam>=2016:
            evszam=int(input('8. feladat: Kérem adja meg az évszámot [2011..2016]: '))
    
            




Feladat=Uzemanyag('uzemanyag.txt')

Feladat.feladat9()

