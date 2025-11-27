nombreEtudiants = int(input("Donnez le nombre d'élèves : "))
moyenne=0.0
somme=0.0
notes = []  #

for i in range(nombreEtudiants):
    note = float(input(f"Donnez la note de l'élèves {i + 1} : "))

    while note < 0 or note > 20:
        for _ in range(10):
            print("NOTE incorrecte 🤯😤😡")

        note = float(input(f"Donnez une note correcte pour l'élève {i + 1} : "))

    notes.append(note)
    somme+= note

moyenne= somme/nombreEtudiants


print("\n======= 📊 Résultats de la classe 📊 =======")
print(f"Moyenne générale : {moyenne:.2f}\n")


print(f"{'N° Étudiant':<12} | {'Note':<6} | {'Écart à la moyenne'}")


for i in range(nombreEtudiants):
    ecart = notes[i] - moyenne
    print(f"{i+1:<12} | {notes[i]:<6.2f} | {ecart:+.2f}")

