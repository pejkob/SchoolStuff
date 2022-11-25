
   
def szokoev(szam):
    if szam%4==0 and szam%100!=0 or szam%400==0:
        return True
    else:
        return False

szam=int(input('Adjon meg egy számot! '))
szokoev(szam)
if szokoev(szam):
    print('A megadott év szökőév')
else:
    print('A megadott év nem szökőév')