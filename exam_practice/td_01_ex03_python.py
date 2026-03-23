#nombre de jours location
jours = int(input("ecrivez le nombre de jours de votre location : "))

#km de la location
km = float(input("ecrivez la km : "))

#prix de la location
prix_location = 0.5 * km + 60 * jours

print("le prix final de la location est : ", prix_location)