prenom_a = input("prenom svp : ")
taille_a = float(input("taille svp : "))
poids_a = float(input("poids svp : "))

prenom_b = input("prenom svp : ")
taille_b = float(input("taille svp : "))
poids_b = float(input("poids svp : "))

plus_corpulent = (taille_a > taille_b) and (poids_a > poids_b)

print(prenom_a, "est plus corpulent que ", prenom_b, "=", plus_corpulent)