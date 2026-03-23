n = int(input("ecrivrez un nombre : "))
somme = 0

while n > 0:
    reste = n % 10
    if reste % 2 == 0:
        somme = somme + reste
    n = n // 10
print(somme)