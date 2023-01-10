def szoValogato(li,reszlet):
    lista=[]
    for elem in li:
        if elem.__contains__(reszlet):
            lista.append(elem)
    return lista

def szoDarab(li,reszlet):
    darab=0
    for elem in szoValogato(li,reszlet):
        darab+=1
    return darab


