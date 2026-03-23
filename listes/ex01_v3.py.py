n = int(input("ecrivez un nombre reels : "))
liste = []

for i in range(n):
    valeur = float(input("entrez un nombre : "))
    liste.append(valeur)
somme = 0
for valeur in liste:
    somme = somme + valeur
moyenne = somme / valeur
print(moyenne)

for i in range(n):
    for j in range(n-1):
        if liste[j] < liste[j+1]:
            liste[j], liste[j+1] = liste[j+1], liste[j]
print("moyenne est : ", moyenne)

if n % 2 == 1:
    medianne = liste[n//2]
else:
    medianne = (liste[n//2] + liste[n//2 - 1]) / 2