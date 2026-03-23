n = int(input("ecrivez un nombre : "))

somme = 0
for i in range(1, n+1, 2):
    somme = somme + i
print(somme)