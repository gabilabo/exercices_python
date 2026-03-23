n = int(input("ecrivez nombre reelles positifs : "))
somme = 0
while n > 0:
    n = int(input("ecrivez un nombre reelles positifs : "))
    somme = somme + n
    if n < 0:
        print("0")
print("la somme de nombres reelles positifs est de : ",somme)