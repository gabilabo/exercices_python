n = int(input("ecrivez un nombre : "))
nbr_original = n
inverse = 0
while n > 0:
    reste = n % 10
    inverse = inverse * 10 + reste
    n = n // 10
if nbr_original == inverse:
    print("palindrome")
else:
    print("pas palindrome")