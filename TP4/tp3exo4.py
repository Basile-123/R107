#PARTIE 1

L1 = [2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7]
max_occ = 0
element = L1[0]

for i in L1:
    occ = L1.count(i)
    if occ > max_occ:
        max_occ = occ
        element = i

print(f"Le nombre le plus frequent dans la liste est le : {element} ({max_occ} x)")


#PARTIE 2


max_occ = 0
element = L1[0]

for i in L1:
    occ = L1.count(i)
    if occ > max_occ:
        max_occ = occ
        element = i

print(f"Le nombre le plus frequent dans la liste est le : {element} ({max_occ} x)")