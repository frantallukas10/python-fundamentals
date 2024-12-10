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

Vzorový výstup pre bonus: 
Bob: 28.0
Hanka: 27.5
Gertruda: 24.0
John: 22.0
Dana: 20.0
Ivan: 20.0
Cyril: 19.5
Alice: 15.0
Filip: 8.0
Emil: 7.5
"""

from collections import defaultdict

papier = defaultdict(lambda: 0.0)

# lambda funkcia

# defaultdict -> 
# https://www.accelebrate.com/blog/using-defaultdict-python
# https://docs.python.org/3.7/library/collections.html#defaultdict-objects


with open('papier.txt') as r:
    r.readline()  # Ignorujeme 1. riadok
    for line in r:
        datum, meno, mnozstvo = line.strip().split(',')
        meno = meno.strip()
        mnozstvo = float(mnozstvo)
        papier[meno] += mnozstvo # Ak meno nie je v slovníku papier, tak sa automaticky pridá, pretože je to defaultdict.

for meno, mnozstvo in sorted(papier.items(), key = (lambda item: item[1]), reverse=True):
    print(f'{meno}: {mnozstvo}')
