notes_str = input("Entrez les notes séparées par des espaces : ")

notes = [float(n) for n in notes_str.split()]

moyenne = sum(notes) / len(notes)
note_max = max(notes)
note_min = min(notes)
notes_triees = sorted(notes)

print(f"Moyenne : {moyenne}")
print(f"Note maximale : {note_max}")
print(f"Note minimale : {note_min}")
print(f"Notes triées : {notes_triees}")