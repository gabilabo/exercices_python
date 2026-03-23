import random
random.seed(None)
allumettes = random.randint(15, 20)

while allumettes > 1:
    print("vous avez encore", allumettes, "allumettes")
   
    retirer = int(input("combien d'allumettes voulez vous retirer? : "))
    
    if 1 <= retirer <= 3 and retirer <= allumettes:
        allumettes = allumettes - retirer
    
        if allumettes == 1:
            print("vous avez gagné!")
            break
        
        retirer_ordi = random.randint(1, 3)
        
        while retirer_ordi >= allumettes:
            retirer_ordi = random.randint(1, 3)
            
        print("l'ordinateur retire", retirer_ordi, "allumettes")
        allumettes = allumettes - retirer_ordi
        
        if allumettes == 1:
            print("l'ordinateur a gagné!")
            break
    else:
        print("choix invalide")