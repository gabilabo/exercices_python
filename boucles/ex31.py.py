import random
random.seed(None)
mystere = random.randint(1, 100)
essais = 0
while True:
    n = int(input("entrez un nombre : "))
    essais = essais + 1
    
    if n == mystere:
        print("bravo! Vous avez trouvé le nombre mystère, le nombre d'essais est de : ", essais, "tentatifs")
        break
    elif n > mystere:
        print("votre chiffre", n, "est plus grand que le nombre mystère")
    else:
        print("votre chiffre", n, "est plus petit que le nombre mystère")