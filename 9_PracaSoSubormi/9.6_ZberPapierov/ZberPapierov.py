"""
Úloha:
Súbor papier.txt obsahuje informácie o zbere papiera - kedy, kto, a koľko kg doniesol. Napíšte program, ktorý načíta tento súbor a spočíta celkovú hmotnosť zozbieraného papiera pre každú osobu. Výsledok vypíše na štandardný výstup, osoby budú zoradené podľa abecedy.

Vzorový výstup:  
Alice: 15.0
Bob: 28.0
Cyril: 19.5
Dana: 20.0
Emil: 7.5
Filip: 8.0
Gertruda: 24.0
Hanka: 27.5
Ivan: 20.0
John: 22.0

Bonus: 
Modifikujte program tak, aby vypisoval ľudí v poradí podľa nazbieraného množstva papiera (od najväčšieho po najmenší).
"""

papier = {}

with open('papier.txt') as r:
    r.readline()  # Ignorujeme 1. riadok
    for line in r:
        datum, meno, mnozstvo = line.strip().split(',')
        meno = meno.strip()
        mnozstvo = float(mnozstvo)
        if meno not in papier:
            papier[meno] = 0.0
        papier[meno] += mnozstvo

for meno, mnozstvo in sorted(papier.items()): # vytvory novy zoradeny zoznam
    print(f'{meno}: {mnozstvo}')
