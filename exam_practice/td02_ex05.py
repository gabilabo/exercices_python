salaire_pere = float(input("ecrivez le salaire pere annuel : "))
salaire_mere = float(input("ecrivez le salaire mere annuel : "))
nbr_enfants = int(input("ecrivez le nombre d'enfants : "))

r = salaire_mere + salaire_pere
adultes = 2
enfants = 0.5

nombre_parts = 2 + (0.5 * nbr_enfants)
qf = r / nombre_parts

if qf <= 5963:
    montant_impot = 0
elif qf <= 11896:
    montant_impot = r * 0.055 - 327.97 * nombre_parts
elif qf <= 26420:
    montant_impot = r * 0.14 - 1339.13 * nombre_parts
elif qf <= 70830:
    montant_impot = r * 0.3 - 5566.33 * nombre_parts
else: 
    montant_impot = r * 0.41 - 13357.63 * nombre_parts 
print("le montant d'impots est de : ", montant_impot)