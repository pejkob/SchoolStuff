szoveg=input('szoveg: ')
szoveg2=input('szoveg2: ')

count=False
if len(szoveg2)>len(szoveg):
    for i in range(len(szoveg2)-1):
        if szoveg2[i]==szoveg[i]:
            count=True

else:
    
    for i in range(len(szoveg)-1):
        if szoveg2[i]==szoveg[i]:
            count=True

print(count)
