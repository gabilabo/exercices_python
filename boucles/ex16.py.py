n = int(input("ecrivez un nombre : "))

compteur = 0
while n > 0:
    n = n // 10
    compteur = compteur + 1
print("le nombre contient : " , compteur, "chiffre(s)")