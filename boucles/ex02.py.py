n =  int(input("ecrivez un nombre : "))
compteur = 0
for i in range(2, n):
   if n % i == 0:
       compteur = compteur + 1
print(compteur)