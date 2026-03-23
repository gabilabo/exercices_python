prix_ht = float(input("entre le prix HT : "))

categorie = input("ecrivez la categorie du produit : ").lower()


if categorie == "alimentaire":
    tva = 0.055    
else:
    tva = 0.20

prix_ttc = prix_ht * (1 + tva)    

print("le prix TTC du produit est : ", prix_ttc)