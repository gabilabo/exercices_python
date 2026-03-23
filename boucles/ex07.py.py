n = int(input("ecrivez un nombre : "))
inverse = 0

while n > 0:
    reste = n % 10
    inverse = inverse * 10 + reste
    n = n // 10
print(inverse)
    