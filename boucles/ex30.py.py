n = int(input("ecrivez un nombre : "))
pluspetit = None
plusgrand = None
premier = True

for i in range(2, n):
    if n % i == 0:
        premier = False
        if pluspetit is None:
            pluspetit = i
        plusgrand = i
if premier:
    print("le nombre est premier")
else:
    print("le nombre n'est pas premier et le plus petit diviseur est : ", pluspetit, "et le plus grand est : ", plusgrand)