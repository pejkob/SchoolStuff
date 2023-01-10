class Kolcsonzes:
    adatsor=[]
    def __init__(self,allomanynev) -> None:


        
        with open(allomanynev,'r',encoding='UTF-8') as f:
            sorok=f.readlines()
            
            for i in range(1,len(sorok)):
                mezonevek=sorok[0].strip('\n').split(';')
                split=sorok[i].strip('\n').split(';')
                self.adatsor.append({
                    mezonevek[0]:split[0],
                    mezonevek[1]:split[1],
                    mezonevek[2]:int(split[2]),
                    mezonevek[3]:int(split[3]),
                    mezonevek[4]:int(split[4]),
                    mezonevek[5]:int(split[5])
                })
    def kiir(self):
        print(self.adatsor,end='\n')
    def elemSzam(self):
        print(f'5. feladat: Napi kölcsönzések száma: {len(self.adatsor)}')
    
    def vezetoNullak(self):
        idostring=''
        if self.adatsor['EÓra']<10:
            idostring='0'+str(self.adatsor['EÓra'])+':'
        else:
            idostring=str(self.adatsor['EÓra'])+':'

        if self.adatsor['EPerc']<10:
            idostring=idostring+'0'+str(self.adatsor['EPerc'])+':'
        else:
            idostring=idostring+str(self.adatsor['EPerc'])+':'

        if self.adatsor['VÓra']<10:
            idostring='0'+str(self.adatsor['VÓra'])+':'
        else:
            idostring=str(self.adatsor['VÓra'])+':'

        if self.adatsor['Vperc']<10:
            idostring=idostring+'0'+str(self.adatsor['Vperc'])+':'
        else:
            idostring=idostring+str(self.adatsor['Vperc'])+':'
            
        return idostring

    def kolcsonzesInfo(self,nev):
      
      van=False
      for sor in self.adatsor:
        if sor['Név']==nev:
            van=True
            print(f'{sor["EÓra"]}:{sor["EPerc"]}-{sor["VÓra"]}:{sor["Vperc"]}')
      if van==False:
        print('Nincs ilyen nevű kölcsönző')
    
    def intervallum(self,intervall):
        iora=intervall.split(':')[0]
        iperc=intervall.split(':')[1]
        for sor in self.adatsor:
            if sor['EÓra']<iora


        
            
            


vizi=Kolcsonzes('kolcsonzesek.txt')
vizi.elemSzam()
nev=input('6. feladat: Kérek egy nevet: ')

vizi.kolcsonzesInfo(nev)
intervall=input('7. Feladat: Adjon meg egy időpontot óra:perc alakban: ')
vizi.intervallum(intervall)