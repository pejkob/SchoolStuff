class Ronk:
    ronkadatok=[]
    def __init__(self,azon,fajta,terfogat,ar,kategoria) -> None:
        self.azon=int(azon)
        self.fajta=fajta
        self.terfogat=float(terfogat)
        self.ar=int(ar)
        self.kategoria=kategoria

        self.ronkadatok.append({
            'azon':azon,
            'fajta':fajta,
            'terfogat':terfogat,
            'ar':ar,
            'kategoria':kategoria
        })

    def tomeg(self,azon):
      
        for sor in self.ronkadatok:
            if azon==sor['azon'] and sor['kategoria']=='keményfa':
            
             return sor['terfogat']*800
             
            if azon==sor['azon'] and sor['kategoria']=='puhafa':
               return sor['terfogat']*500
    
    def osszar(self):
        osszar=0
        for sor in self.ronkadatok:
            if azon==sor['azon'] and sor['kategoria']=='keményfa':
                osszar+=sor['terfogat']*sor['ar']
            else:
                osszar+=sor['terfogat']*sor['ar']
        
        print(f'Az erdészet bevétele {osszar} Ft.')
                
#49500 102000 22800 17600 13020
#204 920
    
    def legolcsobb(self):
        minar=self.ar
        legolcsobbfajta=''
        for sor in self.ronkadatok:
            if sor['ar']<minar:
                minar=sor['ar']
                legolcsobbfajta=sor['fajta']
        
        return legolcsobbfajta

    def tolgy(self):
        with open('tolgy.txt','w',encoding='utf-8') as w:
            for sor in self.ronkadatok:
                if sor['fajta']=='tölgy':
                    w.writelines(str(sor['azon'])+' '+str(sor['terfogat'])+' '+str(sor['ar'])+'\n')

                

        
        
    
    def kiir(self):
        print(self.ronkadatok)

azon=int(input('Kérem az azonosítót: '))
fajta=input('Kérem a fajt: ')
terfogat=float(input('Kérem a térfogatát: '))
ar=int(input('Kérem az árat: '))
kategoria=input('Kérem a kategóriát: ')
ronkok=Ronk(azon,fajta,terfogat,ar,kategoria)
ronkok=Ronk(1,'tölgy',0.9,55000,'keményfa')
ronkok=Ronk(2,'bükk',1.2,85000,'keményfa')
ronkok=Ronk(3,'fenyő',0.6,38000,'puhafa')
ronkok=Ronk(4,'tölgy',0.55,32000,'keményfa')
ronkok.osszar()
bekertaz=int(input('Kérem, adja meg egy rönk azonosítóját! '))
print(f'A(z) {bekertaz} azonosítójú rönk tömege: {ronkok.tomeg(bekertaz)} kg.')
print(f'A legolcsóbb rönk fafaja: {ronkok.legolcsobb()}')
ronkok.tolgy()