import mondatok_alap

print('Adj meg három főnevet!')
index=1
while index<=3:
    bekertszo=input(f'{index}.főnév:')
    print(mondatok_alap.névelő(bekertszo)+' '+bekertszo+' '+mondatok_alap.jelző()+'.')
    index+=1




