minutes_total = int(input("Entrez le nombre de minutes écoulées depuis le début du mois : "))

jour = minutes_total // (24 * 60)

jour_du_mois = jour + 1

print("La date correspond au jour :", jour_du_mois)
