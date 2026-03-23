n = int(input("ecrivez un nombre : "))
produit = 1

while n > 0:
    reste = n % 10
    produit = produit * reste
    n = n // 10
    
print(produit)
    
    