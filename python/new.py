numb=int(input('Adjon meg egy számsort '))
maxnum=0
for i in range(len(numb)):
    if numb[i]<maxnum:
       numb[i]= maxnum

print(numb)

