"""
Úloha:
Pomocou súboru cofactors.json nájdite všetky zlúčeniny, ktoré sú kofaktorom nejaké hydrolázy. (V klasifikácii enzýmov EC tvoria hydrolázy triedu 3, hľadáme teda všetky záznamy, ktoré majú v "EC" uvedené aspoň jedno číslo začínajúce trojkou.)
Hint: Na prehľadné zobrazenie súboru cofactor.json vo VSCode kliknite
pravým tlačidlom na text a vyberte Format document.
Zdroj dat: https://www.ebi.ac.uk/pdbe/api/doc/compounds.html, čast Cofactors

Vzorový výstup:  
Phosphopantetheine
Nicotinamide-adenine dinucleotide
Adenosylcobalamin
Flavin adenine dinucleotide
Tetrahydrofolic acid
Coenzyme A
Flavin Mononucleotide
Menaquinone
Heme
Glutathione
S-adenosylmethionine
Thiamine diphosphate
Pyridoxal 5'-phosphate
"""

import json

with open('cofactors.json') as f:
    cofactors = json.load(f) # nacita JSON zo suboru

selected = []

for compound, data in cofactors.items():
    enzymes = data[0].get('EC', []) # riesi aj chybajuce kluce
    if any(enzyme.startswith('3.') for enzyme in enzymes):
        selected.append(compound)

print(*selected, sep='\n') # vytiahne vsetky prvky z iterovaneho objektu