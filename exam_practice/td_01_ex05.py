total_secondes = int(input("ecrivez un nombre des secondes : "))

heures = total_secondes // 3600
reste = total_secondes % 3600
minutes = reste // 60
secondes = reste % 60

print(total_secondes, "correspondent a : ", heures, minutes, secondes)
