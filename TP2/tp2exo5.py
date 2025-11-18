nb = int(input("Entré un nombre entier : "))
for i in range(5):
    if nb > 0:
        if nb %2 == 0:
            print("Le nombre est positif et pair")
        else:
            print("Le nombre est positif et impaire")

    elif nb < 0:
        if nb %2 == 0:
            print("Le nombre est négatif et pair")
        else:
            print("Le nombre est négatif et impaire")

    else:
        print("Le nombre est zéro (et il est pair)")