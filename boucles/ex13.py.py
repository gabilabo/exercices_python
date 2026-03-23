n = int(input("ecrivez un nombre : "))
compteur = 0

for i in range(1, n+1):
    if n % i == 0:
        compteur = compteur + 1
        
print(compteur)