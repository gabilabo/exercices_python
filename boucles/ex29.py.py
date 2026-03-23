n  = int(input("ecrivez un nombre : "))
premier = True

for i in range(2, n):
   if n % i == 0:
        premier = False
if premier:
    print("il est premier")
else:
    print("il n'est pas premier")
        