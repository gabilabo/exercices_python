n= int(input("ecrivez un nombre : "))

zero_trouve = False
while n > 0:
    reste = n % 10
    
    if reste == 0:
        zero_trouve = True
    n = n // 10
if zero_trouve:
    print("le nombre contient 0")
else:
    print("le nombre ne contient pas 0")