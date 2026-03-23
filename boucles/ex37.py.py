n = int(input("ecrivez un nombre : "))
for i in range(2, n):
    if n % i == 0:
        print(i)