class Termék:
    adatsorok=[]
    def __init__(self,allomanynev) -> None:
        with open(allomanynev,'r',encoding='utf-8') as f:
            sorok=f.readlines()
            for sor in sorok:
                splittelt=sor.strip('\n').split(';')
                self.adatsorok.append({
                    'ID':splittelt[0],
                    'Termek tipus':splittelt[1],
                    'Gyarto':splittelt[2],
                    'Tipus':splittelt[3],
                    'Beszallito':splittelt[4],
                    'Ar':splittelt[5],
                    'Kiszereles':splittelt[6],
                    'Van-e':splittelt[7]


                 })
    
    def DarabLeker(self):
        termekSzam=0
        for i in range(len(self.adatsorok)):
            if self.adatsorok[i]['Kiszereles']!='':
                termekSzam+=1
        return termekSzam
    
    def __str__(self) -> str:
        
        print(self.adatsorok)

    def LegdragabbTermek(self):
        maxar=int(self.adatsorok[0]['Ar'])
        maxindex=0
        for i in range(len(self.adatsorok)):
            if int(self.adatsorok[i]['Ar'])>maxar:
                maxindex=int(self.adatsorok[i]['ID'])-1
        
        with open('Legdragabb.txt','w',encoding='utf-8') as w:
             w.writelines(f'{self.adatsorok[maxindex]}\n')


   

newtermek=Termék('termekek.txt')

newtermek.__str__()
print(f'Raktárban lévő termékek száma: {newtermek.DarabLeker()}')
newtermek.LegdragabbTermek()
    