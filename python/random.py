import random
with open('kimenet.txt','w',encoding='UTF-8') as f:
    for i in range(100):
        rnd=random.randint(0,100)
        f.write(f'{str(rnd)}\n')

