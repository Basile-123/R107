a=int(input("merci de saisir la première valeurs: "))
b=int(input("merci de saisir la deuxième valeurs: "))
c=int(input("merci de saisir la troisième valeurs: "))
print("Avant permutation")
print(f"Les valeurs entrees sont : a = {a}, b = {b} et c = {c}" )
d=a
a=c
c=b
b=d

print("Aprés permutation")
print(f"Les valeurs permutees sont : a = {a}, b = {b} et c = {c}" )
print("passer une bonne journée")
