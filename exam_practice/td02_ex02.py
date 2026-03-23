jour = int(input("ecrivez le nombre des jours : "))

km = int(input("entrez la kilometrage : "))

if (jour > 30):
    prix = 60 * jour
else:
    prix = 50 * jour + 0.7 * km
    
print("le prix de la location est de : ", prix)