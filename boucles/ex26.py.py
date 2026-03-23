n1 = int(input("ecrivez un nombre : "))
n2 = int(input("ecrivez un nombre : "))

if n1 >= n2:
    print("erreur")
else:
    for i in range(n1+1, n2):
        print(i, end=" ")