dictionnaire = {}

while True:
    mot = input("ecrivez un mot : ").upper()
    if mot == "STOP":
        break
    if mot not in (dictionnaire):
        dictionnaire[mot] = 1
    else:
        dictionnaire[mot] = dictionnaire[mot] + 1
        
for mot, nombre in dictionnaire.items():
    print(mot + " = " + str(nombre))