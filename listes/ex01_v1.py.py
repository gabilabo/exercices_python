n = int(input("ecrivez un nombre reel : "))
liste = []
for i in range(n):
    valeur = float(input("ecrivez un nombre reel : "))
    liste.append(valeur)
somme = 0
for valeur in liste:
    somme = somme + valeur

moyenne = somme / len(liste)
print(moyenne)
for i in range(len(liste)):
    for j in range(len(liste)-1):
       if liste[j] < liste[j+1]:
           liste[j], liste[j+1] = liste[j+1], liste[j]
print(liste)
    
if n % 2 == 1:
    mediane = liste[n//2]
else:
    mediane = (liste[n//2] + liste[n//2 - 1]) / 2
print(mediane)
    
        