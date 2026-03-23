liste = []
nbr_perso = int(input("ecrivez un nombre de personnes : "))

for i in range(nbr_perso):
    nom = input("ecrivez votre nom : ")
    taille = float(input("ecrivez la taille : "))
    poids = float(input("ecrivez le poids : "))
    
    personne = {"nom": nom, "taille": taille, "poids": poids}
    liste.append(personne)
    
imc_min = 1000    
for personne in liste:
    nom = personne["nom"]
    taille = personne["taille"]
    poids = personne["poids"]
        
    taille_m = taille / 100
    imc = poids / (taille_m ** 2)
        
    print(nom, taille, poids, imc)
      

 
    if imc < imc_min:
         imc_min = imc
         nom_min = nom
print("le IMC le plus faible : ", nom_min, imc_min)