
#A
n = int(input("Donner un nombre : "))

somme = 0
for i in range(n + 1):
    somme += i

print("Somme =", somme)

#B
valeur = 0

while valeur != 100:
    valeur = int(input("Entrez une valeur : "))

print("Fin")

#C
inf_10 = 0
entre_10_15 = 0
sup_15 = 0

for i in range(10):
    valeur = -1
    while valeur < 0 or valeur > 20:
        valeur = float(input("Entrez une valeur entre 0 et 20 : "))

    if valeur < 10:
        inf_10 += 1
    elif valeur < 15:
        entre_10_15 += 1
    else:
        sup_15 += 1

print("Inférieur à 10 :", inf_10)
print("Entre 10 et 15 :", entre_10_15)
print("Supérieur ou égal à 15 :", sup_15)


#C
x = float(input("Entrez un valeur de x : "))
somme = 0
n = 0

while somme + n + 1 <= x:
    n += 1
    somme += n
print(f"N = {n}")
print(f"Somme = {somme}")
somme = 0
for i in range(n + 1):
    somme += i
print(f"Somme = {somme}")
