n = int(input("ecrivez un nombre : "))
somme = 0
for i in range(1, n):
    if n % i == 0:
        somme = somme + i
if somme == n:
    print("nombre parfait")
else:
    print("pas parfait")