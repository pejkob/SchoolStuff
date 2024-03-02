import random
def névelő(szó):
    magánhagnzók='aáeéiíoóöőuúüű'
    if szó[0].lower() in magánhagnzók:
       return 'Az'
    
    else:
        return 'A'
    # Egészítse ki a függvényt a visszatérést végző résszel!

def jelző():
    return random.choice(['piros','nagy','könnyed'])