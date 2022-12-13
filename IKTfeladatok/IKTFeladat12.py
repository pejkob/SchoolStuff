szoveg=input('szoveg: ')
szoveg2=input('szoveg2: ')

count=0
if len(szoveg2)>len(szoveg):
    for i in range(len(szoveg)):
        if szoveg2[i]==szoveg[i]:
            count+=1

else:
    
    for i in range(len(szoveg2)):
        if szoveg[i]==szoveg2[i]:
            count+=1

print(count)
