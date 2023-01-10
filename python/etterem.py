class Asztal:
    etteremadatok=[]
    
    def __init__(self) -> None:
        
        with open('asztalok.txt','r',encoding='utf-8') as f:
            sorok=f.readlines()
            
            for sor in sorok:
                splittelt=sor.strip('\n').split('\t')
                foglalt=splittelt[3]+splittelt[4]+splittelt[5]+splittelt[6]+splittelt[7]+splittelt[8]+splittelt[9]+splittelt[10]+splittelt[11]+splittelt[12]+splittelt[13]+splittelt[14]+splittelt[15]+splittelt[16]+splittelt[17]+splittelt[18]+splittelt[19]+splittelt[20]+splittelt[21]+splittelt[22]+splittelt[23]
                self.etteremadatok.append({
                    'Asztal száma':int(splittelt[0]),
                    'Férőhelyek száma':int(splittelt[1]),
                    'Terem':splittelt[2],
                    'Foglalás':foglalt
                })
    
    def kiir(self):
        print(self.etteremadatok)
    
    def foglalasok(self):
        result=[]
        ertekek=0
        for sor in self.etteremadatok:
            for ertek in sor['Foglalás']:
                if ertek==1:
                    ertekek+=1
            
        result.append(sor['Asztal száma'])
        print(f'A legforgalmasabb asztal: {result}')
    
    def foglalt(self,asztal,ido):
        ora=ido.split(':')[0]
        perc=ido.split(':')[1]
        kulonbseg=int(ora)-12
        oraindex=int((kulonbseg*2)+1)
        if int(perc)==30:
            oraindex+=1
       
        for sor in self.etteremadatok['Asztal száma']:
            if sor['Asztal száma']==asztal and sor['Foglalás'][oraindex]==0:
                return False
            else:
                return True
    
    def foglalt_orak(self):
        orakszama=0
        asztaladat=[]
        for sor in self.etteremadatok:
            for ertek in sor['Foglalás']:
                if ertek==1:
                    orakszama+=1/2
            asztaladat.append(orakszama)
        asztaladat.append(sor['Asztal száma'])

        with open('foglalt_orak.txt','w',encoding='utf-8') as w:
            w.writelines(str(asztaladat))


                
        



asztalok=Asztal()
asztalok.kiir()
asztalszam=input('Adjon meg egy asztal számot! ')
idopont=input('Adjon meg egy időpontot! ')
#print(asztalok.foglalt(asztalszam,idopont))

asztalok.foglalt_orak()
asztalok.foglalasok()
