from random import randint

pile_count = 0
face_count = 0

for i in range(5):
    nb = randint(1, 100)
    print(f"Nombre tiré : {nb}")

    if nb <= 50:
        print("Pile !")
        pile_count += 1
    else:
        print("Faces !")
        face_count += 1

    if pile_count == 5 or face_count == 5:
        print("Va jouer au loto !!!")
        break