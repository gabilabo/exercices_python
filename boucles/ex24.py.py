n = int(input("ecrivez un nombre : "))
max = 0
while n > 0:
    reste = n % 10

    if reste > max:
        max = reste
    n = n // 10
print(max)