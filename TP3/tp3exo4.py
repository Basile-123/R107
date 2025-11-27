

n = int(input("Entrez un nombre : "))
choix = input("Boucle for ou while : ")

if choix == "for":

    factorielle = 1

    for i in range(1, n + 1):
        factorielle *= i

        print(f"{i}! = {factorielle}")

    print(f"Résultat : {factorielle}")


elif choix == "while":

    factorielle = 1

    i = 1
    while i <= n:
        factorielle *= i

        print(f"{i}! = {factorielle}")
        i += 1

    print(f"Résultat : {factorielle}")

else:
    print("Choix invalide")