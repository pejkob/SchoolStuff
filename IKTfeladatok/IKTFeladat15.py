tnev=input('Adja meg a teljes nevét! ')
monogram=''

for betu in tnev:
    asd=betu.isupper()
    if asd:
        monogram+=betu+'.'
    
    if betu=='-':
        monogram+='-'
    
    


print(monogram)