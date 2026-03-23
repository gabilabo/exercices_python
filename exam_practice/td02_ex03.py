jour = int(input("ecrivez le nombre de jour : "))

km = int(input("ecrivez la kilometrage : "))

code = int(input("ecrivez le cod du vehicule : "))

if (jour > 30):
    prix = 60 * jour
    print("le prix de la location est de : ", prix)
elif code == 1:
    prix = 70 * jour + 0.5 * km
    print("le prix de la location est de : ", prix)
elif code == 2:
    prix = 60 * jour + 1.2 * km
    print("le prix de la location est de : ", prix)
else:
    print("erreur")