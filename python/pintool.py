def prim_e(n):
    if n==1:
        return False
    for i in range(2,n):
         
         if n%i==0:
            return False
    
    return True

def fugveny(db):
    lista=[]
    szam=2
    while len(lista)<db:
        if prim_e(szam):
            lista.append(szam)
        szam+=1

        
    return lista


print(fugveny(15))