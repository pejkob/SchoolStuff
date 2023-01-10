szelesseg=int(input('Kérem, adja meg az akvárium szélességét egész centiméterben: '))
hosszusag=int(input('Kérem, adja meg az akvárium hosszúságát egész centiméterben: '))
magassag=int(input('Kérem, adja meg az akvárium magasságát egész centiméterben: '))

def halHossz():

   print(f'Az akváriumban összesen {szelesseg*hosszusag*magassag/1000} cm hal lehet.')

halHossz()

akvszel=50
akvhossz=70
akvmag=30

magassagok=[30,35,40,45,50]
magertek=[]
while akvmag<=50:
    magertek.append(((akvhossz*akvszel*akvmag)/1000)/3)
    akvmag+=5


print(f'Ha a magasság: {magassagok[0]}cm, akkor {magertek[0]} db hal telepíthető')
print(f'Ha a magasság: {magassagok[1]}cm, akkor {round(magertek[1])} db hal telepíthető')
print(f'Ha a magasság: {magassagok[2]}cm, akkor {round(magertek[2])} db hal telepíthető')
print(f'Ha a magasság: {magassagok[3]}cm, akkor {round(magertek[3])} db hal telepíthető')
print(f'Ha a magasság: {magassagok[4]}cm, akkor {round(magertek[4])} db hal telepíthető')


#x*80*35/1000/4=40
#x=57,14
akvariumhossz=80
akvariummagassag=35
akvariumszelesseg=40/80/35*1000*4


print(f'A szélességnek minimum {round(akvariumszelesseg)+1} cm-nek kell lennie.')