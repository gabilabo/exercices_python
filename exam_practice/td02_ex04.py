a = float(input("ecrivez un nombre : "))

b =  float(input("ecrivez un nombre : "))

operateurs = input("choisissez un operateur (+, -, *, /) : ")

if operateurs not in ("+", "-", "*", "/"):
    print("erreur")
elif operateurs == "/" and b == 0:
    print("erreur")
else:
    if operateurs == "+":
        resultat = a + b
        print(a, operateurs, b, "=", resultat)
    elif operateurs == "-":
        resultat = a - b 
        print(a, operateurs, b, "=", resultat)
    elif operateurs == "*":
        resultat = a * b
        print(a, operateurs, b, "=", resultat)
    else:
        resultat = a / b
        print(a, operateurs, b, "=", resultat)