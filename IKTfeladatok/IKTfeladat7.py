karakter=input('Adjon meg egy karaktert! ')
angolabc=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
sum=0
while karakter in angolabc:
    karakter=input('Adjon meg egy karaktert! ')
    if karakter.islower():
        sum+=1

print(f'Ennyi karakter volt kisbetűs {sum}')

