n = int(input("ecrivez un nombre : "))
somme = 0
while n > 0:
    reste = n % 10
    somme = somme + reste
    n = n // 10
print(somme)
    
