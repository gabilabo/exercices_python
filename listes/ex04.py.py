dictionnaire = {}
while True:
    cle = input("entrez une clé : ")
    
    if cle == "STOP":
        break
    
    if cle in dictionnaire:
        print("erreur")
    else:
        valeur = input("entrez une valeur : ")
        dictionnaire[cle] = valeur
        
if len(dictionnaire) > 0:
            print(dictionnaire.keys())
            print(dictionnaire.values())
            print(dictionnaire.items())
            