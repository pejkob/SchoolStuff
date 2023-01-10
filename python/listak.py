import random
from traceback import print_tb

listaten=[]
listatwen=[]

for i in range(10):
    listaadat=random.randint(35,45)
    listaten.append(listaadat)


for i in range(20):
    listaadat=random.randint(35,45)
    listatwen.append(listaadat)

print(listaten)
print(listatwen)

kozoslista=[]
for elem in listaten:
    if elem in listatwen:
        if not kozoslista.__contains__(elem):
            kozoslista.append(elem)
    else:
        print('Üres halmaz')    

print(kozoslista)