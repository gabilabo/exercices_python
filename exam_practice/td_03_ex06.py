import random
random.seed(None)
mystere = random.randint(1, 100)

essais = 0

while True:
    n = int(input("ecrivez un nombre : "))
    essais += 1
    if n == mystere:
        print("Bravo!", "le nombre d'essais est : ", essais)
        break
    elif n > mystere:
        print("votre chiffre : ", n," est plus grand que le nombre mystère")
    else:
        print("votre chifre : ", n, " est plus petit que le nombre mistère")