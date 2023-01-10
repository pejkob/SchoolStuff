from pickle import TRUE


def eljaras(betu1,betu2):
    abc="abcdefghijklmnopqrstuvwxyz"
    return abc.__contains__(betu1+betu2) or abc.__contains__(betu2+betu1)

def tartalmaz(bemenet):
    eredmeny=False
    for i in range(len(bemenet)-1):
        if eljaras(bemenet[i],bemenet[i+1]):
            eredmeny=TRUE
    return eredmeny

szoveg=input('Kérem adjon meg egy szöveget')
if tartalmaz(szoveg):
    print('Tartalmaz')
else:
    print('Nem tartalmaz')
