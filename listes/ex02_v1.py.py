liste = []
while True:
    mot = input("entrez un mot : ").upper()
    if mot == "STOP":
        break
    liste.append(mot)
    
for i in range(1, len(liste)):
    cle = liste[i]
    j = i - 1

    while j>= 0 and liste[j] > cle:
        liste[j+1] = liste[j]
        j = j - 1
        
    liste[j+1] = cle
print(liste)

dictionnaire = []
for mot in liste:
    if mot not in dictionnaire:
        dictionnaire.append(mot)
        
for mot in dictionnaire:        
    print(mot, "=", liste.count(mot))