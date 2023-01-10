class pilotak:
    def __init__(self,nev,sz_datum,nemzetiseg,rajtszam) -> None:
        self.nev=nev
        self.sz_datum=sz_datum
        self.nemzetiseg=nemzetiseg
        self.rajtszam=rajtszam
    
    versenyzok=[]
    with open('pilotak.csv','r',encoding='utf-8') as f:
        sorok=f.readlines()
        for i in range(1,len(sorok)):
            splitted=sorok[i].strip('\n').split(';')
            if len(splitted[3])>4:
                versenyzok.append({
                    'Nev':splitted[0],
                    'Sz_Datum':splitted[1],
                    'Nemzetiseg':splitted[2],
                    'Rajtszam':int(splitted[3])
                })
            else:
                 versenyzok.append({
                    'Nev':splitted[0],
                    'Sz_Datum':splitted[1],
                    'Nemzetiseg':splitted[2],
                    
                })

        
    def kiir(self):
        print(self.versenyzok)

