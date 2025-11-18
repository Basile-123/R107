base=4
fromage=800
eau=2
ail=2
pain=400

confive=int(input("Vous étes combien a manger :"))
fromage2=fromage * confive / base
eau2=eau * confive /base
ail2=ail * confive /base
pain2=pain * confive /base

print(f"\nPour faire une fondue fribourgeoise pour {confive} personnes, il vous faut :")
print(f"- {fromage2} gr de fromage")
print(f"- {eau2} dl d'eau")
print(f"- {ail2} gousse(s) d'ail")
print(f"- {pain2} gr de pain")
print("Bonne appétie")
