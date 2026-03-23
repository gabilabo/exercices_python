n = int(input("ecrivez un nombre : "))

plus_petit = None
plus_grand = None
premier = True

for i in range (2, n):
    if n % i == 0:
        premier = False
        if plus_petit is None:
            plus_petit = i
        plus_grand = i
if premier:
    print("le nombre est premier") 
else:
    print("le numero n'est pas premier, le diviseur plus petit est : ", plus_petit, "et le diviseur plus grand est : ", plus_grand)       