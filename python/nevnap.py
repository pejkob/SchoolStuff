fnev=input('Az ön neve: ')
nevnap=input('Kinek van ma nevnapja?')

if fnev==nevnap:
    print('Hisz önnek névnapja van! Boldog névnapot kívánok!')
else:
    print('Ugyan nincs névnapja, de köszöntse ', fnev ,' nevű ismerőseit!')




tnev=input('Az ön teljes neve: ')
tnevnap=input('Kinek van ma nevnapja?')
x=tnev.split(' ')[1]

print(x)

if x==tnevnap:
    print('Hisz önnek névnapja van! Boldog névnapot kívánok!')
else:
    print('Ugyan nincs névnapja, de köszöntse ', tnevnap ,' nevű ismerőseit!')