import random
random.seed(None)
allumettes = random.randint(15, 20)
print("allumettes au depart : ", allumettes)

while allumettes > 1:
    print(allumettes)
    n = int(input("ecrivez un nombre entre 1 et 3 : "))
   
    while n < 1 or n > 3 or n > allumettes - 1:
        n = int(input("ecrivez un nombre entre 1 et 3 : "))

    allumettes = allumettes - n

    if allumettes == 1:
        print("vous avez gagné!")
        break
   
    max_ordi = min(3, allumettes - 1)
    ordi = random.randint(1, max_ordi)
    print("L'ordinateur a retiré : ", ordi, "allumettes" ) 
    allumettes = allumettes - ordi 
    
    if allumettes == 1:
        print("L'ordinateur a gagné!")
        break