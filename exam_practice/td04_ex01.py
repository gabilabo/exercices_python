n = int(input("ecrivez la taille d'une liste : "))


liste = []

for i in range(n):
    valeur = int(input("ecrivez un nombre : "))
    liste.append(valeur)
    
somme = 0

for element in liste:
    somme = somme + element
if len(liste) > 0:
    moyenne = somme / len(liste)
    print("la moyenne est : ", moyenne)

for i in range(len(liste)):
    for j in range(len(liste) - 1):
        if liste[j] < liste[j+1]:
            temp = liste[j]
            liste[j] = liste[j+1]
            liste[j+1] = temp
            
if len(liste) % 2 != 0:
    mediane = 