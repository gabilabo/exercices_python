n = int(input("ecrivez un nombre  : "))
produit  = 1

while n > 0:
    reste = n % 10
    if reste % 2 == 1:
        produit = produit * reste
    n = n //10
print("le produit est : ", produit)