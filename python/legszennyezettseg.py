with open('Miskolc Lavotta-PM10.csv','r',encoding='UTF-8') as f:
    sorok=f.readlines()
    adatok=[]
    for sor in sorok:
        seged=sor.split()
        if len(seged)<3:
            
            adatok.append(
                {
                    'Dátum':seged[0],
                    'Idő':seged[1],
                    'Érték':-1
                }
            )
        else:
              
            adatok.append(
                {
                    'Dátum':seged[0],
                    'Idő':seged[1],
                    'Érték':int(seged[2])
                }
            )  
    def kiir():
        print(adatok)
#Volt-e olyan időpont, amikor a mért érték meghaladta az egészségügyi határértéket?
#eldöntés tétele
    def volte():
        index=0
        while len(adatok)>index and adatok[index]['Érték']<=50:
            index+=1

        if len(adatok)>index:
            print('Van határértéket meghaladó érték')
        else:
            print('Nincs határértéket meghaladó érték')
#megszámlálás tétele
    def hanyszor():
        sum=0

        for sor in adatok:
            if sor['Érték']>50:
                sum+=1

        print(f'Ennyiszer haladta meg a határértéket {sum}')
    
    def outputlist():
        output=[]
        for i in range(len(adatok)) :
            
            if adatok[i]['Érték'] > 50 and adatok[i]['Dátum'] not in output:
                output.append(adatok[i]['Dátum'])
        print(output)
    def ora(o):
        return int(o.split(':')[0])

    def durvaOra():
        tullepesek=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for sor in adatok:
            if sor['Érték'] >50:
                tullepesek[ora(sor['Idő'])]+=1
        print(tullepesek)
        index=0
        while tullepesek[index]!=max(tullepesek):
            index+=1
        print(index)

    def hianyos():
        #mely napokon nem volt mérési érték
        hianyosList=[]
        for elem in adatok:
            if elem['Érték']==-1:
                hianyosList.append(elem['Dátum'])
        print(hianyosList)
    f.close()

kiir()
volte()
hanyszor()
outputlist()
durvaOra()
hianyos()
