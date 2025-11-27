
from time import*

n = int(input("Entrez un nombre : "))

for i in range(n, -1, -1):
    print(i)
    sleep(1)
print(" FIIIN !")


### VERSION WHILE

i = n
while i >= 0:
    print(i)
    sleep(1)
    i -= 1
print("FIIIN !")