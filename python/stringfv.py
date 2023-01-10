
inp=input('Szöveg:')

for i in range(len(inp)):
    if i%2==1:
        print(inp[i])

inp2=input('Még egy szöveg:')
betu=input('Megadott betű:')

if inp2.__contains__(betu):
    print('A megadott betű megtalálható a szövegben')
else:
    print('A megadott betű nem megtalálható a szövegben')


inp3=input('Szöveg3:')
maganhangzok='aeiou'

for i in range(len(inp3)):
   for j in range(len(maganhangzok)):
    if inp3.__contains__(maganhangzok[j]):
        print('van benne maganhangzo')
        break
    else:
        print('nincs benne')
        break
