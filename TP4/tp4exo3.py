

nMax = 10

n = int(input(f"Quelle est la taille de vos vecteurs [entre 1 et {nMax}] ? "))

while n < 1 or n > nMax:
    n = int(input(f"Valeur incorrecte ! Merci de resaisir la taille [entre 1 et {nMax}] : "))

v1 = []
v2 = []

print("Saisie du premier vecteur :")
for i in range(n):
    val = int(input(f"v1[{i}] = "))
    v1.append(val)

print("Saisie du second vecteur :")
for i in range(n):
    val = int(input(f"v2[{i}] = "))
    v2.append(val)

produit = 0
for i in range(n):
    produit += v1[i] * v2[i]

print(f"Le produit scalaire de v1 par v2 vaut {produit:.1f}")
