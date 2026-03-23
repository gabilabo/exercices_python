n = int(input("ecrivez un nombre : "))

premier = True

if n <= 1:
    print("erreur")
else:
    for i in range(2, n):
        if n % i == 0:
            premier = False
            break
        if premier:
            print("n est premier")
        else:
            print("n n'est pas premier")
    
