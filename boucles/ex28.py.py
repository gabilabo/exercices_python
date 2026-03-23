n = int(input("ecivez un nombre > 2 : "))

if n < 2:
    print("erreur")
else:
    for i in range(2, n):
        if n % i == 0:
            print(i)