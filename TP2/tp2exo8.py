while True:
    a = float(input("Entrez un nombre décimale : "))

    appartien = (((a == 2) or (a > 2 and a < 3)) or (a > 0 and (a < 1 or a == 1)) or ((a == -10) or (a > -10 and (a < -2 or a == -2))))

    if appartien:
        print(f"{a} appartient à I")

    else:
        print(f"{a} n'appartient pas à I")