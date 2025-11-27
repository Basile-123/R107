date = input("Entrez une date au format jj/mm/aaaa : ")

# Vérification du format général
if len(date) != 10 or date[2] != "/" or date[5] != "/":
    print("Format incorrect ! Merci de saisir une date sous la forme jj/mm/aaaa.")
else:
    # Extraction des parties
    jour_str, mois_str, annee_str = date.split("/")

    # Vérification que ce sont bien des chiffres
    if not (jour_str.isdigit() and mois_str.isdigit() and annee_str.isdigit()):
        print("Format incorrect : la date doit contenir uniquement des chiffres.")
    else:
        jour = int(jour_str)
        mois = int(mois_str)
        annee = int(annee_str)

        # Vérification du mois
        if mois < 1 or mois > 12:
            print("Date incorrecte : mois invalide.")
        else:
            # Détermination du nombre de jours dans le mois
            if mois in [1, 3, 5, 7, 8, 10, 12]:
                max_jour = 31
            elif mois in [4, 6, 9, 11]:
                max_jour = 30
            else:  # février
                if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
                    max_jour = 29
                else:
                    max_jour = 28

            # Vérification du jour
            if jour < 1 or jour > max_jour:
                print("Date incorrecte : jour invalide.")
            else:
                print("Date correcte :", f"{jour:02d}/{mois:02d}/{annee}")
