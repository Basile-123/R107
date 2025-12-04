

texte = input("Entrez un mot ou une phrase : ")

nettoye = texte.replace(" ", "").lower()


if nettoye == nettoye[::-1]:
    print("C'est un palindrome !")

else:
    print("Ce n'est pas un palindrome")


# sans [::-1]
inverse = ""
for caractere in nettoye:
    inverse = caractere + inverse

if nettoye == inverse:
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome")
