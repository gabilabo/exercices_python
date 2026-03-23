a = int(input("entrée l'anée > 0 : "))

if a % 400 == 0:
    print("année bissextile")
elif a % 100 == 0:
    print("non bissextile")
elif a % 4 == 0:
    print("année bissextile")
else:
    print("non bissextile")