import random



sor=[]
ujsor=[]

for i in range(15):
    adat=random.randint(10,20)
    sor.append(adat)
    if(adat<=16 and adat>=14 or adat==20 or adat==10):
        ujsor.append(adat)

print('2.feladat',sor)
print('3.feladat',ujsor)



