import random
lottoSzamok=[]
for i in range(5):

    rnd=random.randint(1,100)
    if lottoSzamok.__contains__(rnd):

        rnd=random.randint(1,100)
    else:
        lottoSzamok.append(rnd)

print(lottoSzamok)