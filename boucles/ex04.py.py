n = int(input("ecrivez des nombres positifs : "))
somme = 0
compteur = 0
while n > 0:
    compteur = compteur + 1
    somme = somme + n
    n = int(input("ecrivez des nombres positifs : "))
    
if compteur > 0:
    moyenne = somme / compteur
    print(moyenne)