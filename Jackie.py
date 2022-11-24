class Jackie:
    adatok=[]
    def __init__(self) -> None:
        with open('jackie.txt','r',encoding='utf-8') as f:
            
            sorok=f.readlines()
         
            elso=sorok[0].strip('\uffef').strip('\n').split('\t')
          
            
            for i  in range(1,len(sorok)):
                
                tagolt=sorok[i].strip('\uffef').strip('\n').split('\t')
                self.adatok.append({
                    elso[0]:tagolt[0],
                    elso[1]:int(tagolt[1]),
                    elso[2]:int(tagolt[2]),
                    elso[3]:int(tagolt[3]),
                    elso[4]:int(tagolt[4]),
                    elso[5]:int(tagolt[5]),
                })
            f.close()
    def kiir(self):
        print(self.adatok)
    def feladat3(self):
        print(f'3. feladat: {len(self.adatok)}')
    
    def feladat4(self):
        maxraces=self.adatok[0]['races']
        maxindex=0
        for i in range(len(self.adatok)):
            if self.adatok[i]['races']>maxraces:
                maxraces=self.adatok[i]['races']
                maxindex=self.adatok[i]['\ufeffyear']
        return maxindex
    def feladat5(self):
        hatvanas=0
        hetvenes=0
        for sor in self.adatok:
            if int(sor['\ufeffyear'])<1970:
                hatvanas+=sor['wins']
            else:
                hetvenes+=sor['wins']
        print(f'5. feladat:\n\t70-es évek: {hetvenes} megnyert verseny\n\t60-as évek: {hatvanas} megnyert verseny')


    def feladat6(self):
        with open('jackie.html','w',encoding='utf-8') as w:
            parts=["<!DOCTYPE html>",
                    "<html lang='en'>",
                    "<head>",
                    "</head>",
                    "<style>td {border:1px solid black;} </style>"
                    "<body>",
                    "<h1>Jackie Stewart</h1>",
                    "<table>",
                    "<tr><td>1973</td><td>18</td><td>6</td></tr>",
                    "<tr><td>1972</td><td>11</td><td>4</td></tr>",
                    "<tr><td>1971</td><td>26</td><td>8</td></tr>",
                    "<tr><td>1970</td><td>20</td><td>3</td></tr>",
                    "<tr><td>1969</td><td>19</td><td>9</td></tr>",
                    "<tr><td>1968</td><td>12</td><td>4</td></tr>",
                    "<tr><td>1967</td><td>27</td><td>3</td></tr>",
                    "<tr><td>1966</td><td>26</td><td>6</td></tr>",
                    "<tr><td>1965</td><td>18</td><td>2</td></tr>",
                    "<tr><td>1964</td><td>14</td><td>8</td></tr>",
                    "</table>"
                    "</body>",
                    "</html>",]
            w.writelines(parts)
            w.close()
        
jack=Jackie()
jack.kiir()
jack.feladat3()
print(f'4. feladat: {jack.feladat4()}')
jack.feladat5()
jack.feladat6()