import random

rnd=random.randint(99,1000)
osztok=[]
print(rnd)
oszto=1
for i in range(rnd):
    
    if rnd%oszto==0:
        osztok.append(oszto)
    oszto+=1
    


print(osztok)

    
