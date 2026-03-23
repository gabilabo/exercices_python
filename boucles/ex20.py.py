n = int(input("entrez un nombre : "))

compteur = 0

while n > 0:
    reste = n % 10
    if n % 2 == 0:
        compteur = compteur + 1
    n = n // 10
print(compteur)