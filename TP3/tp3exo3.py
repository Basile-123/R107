from random import*

mystere = randint(0, 100)
compteur = 0
proposition = 0

print("Devinez le nombre entre 0 et 100")

while proposition != mystere:
    proposition = int(input("Votre proposition : "))
    compteur += 1

    if proposition < mystere:
        print("Plus grand")

    elif proposition > mystere:
        print("Plus petit")

    else:
        print("Bravo ! Trouvé en", compteur, "essais")
