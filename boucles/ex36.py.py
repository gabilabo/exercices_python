n1 = int(input("ecrivez un nombre  : "))
plus_grand = n1
for i in range(4):
    n1 = int(input("ecrivez un nombre : "))
    if n1 > plus_grand:
        plus_grand = n1
print(plus_grand)        
        