n1 = int(input("ecrivez un nombre : "))
plus_grand = n1

for i in range(4):
    n2 = int(input("ecrivez un nombre : "))
    if n2 > plus_grand:
        plus_grand = n2
print(plus_grand)