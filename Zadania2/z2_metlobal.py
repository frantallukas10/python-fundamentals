# Napíšte definíciu funkcie celkove_skore, ktorá zoberie ako parameter reťazec s informáciami o metlobalovom turnaji. Tento reťazec bude obsahovať záznamy oddelené bielymi znakmi. Každý záznam zodpovedá jednému zápasu (názvy súperiacich tímov a ich skóre Funkcia vráti slovník, v ktorom kľúče sú názvy tímov a hodnoty sú ich celkové skóre.
# (Na poradí kľúčov v slovníku nezáleží, v testoch je použitá funkcia pprint, ktorá kľúče zoradia podľa Abecedy.)

from typing import List, Dict
from pprint import pprint


'''Gryffindor:Hufflepuff:200:120  Ravenclaw:Slytherin:180:210 
Hufflepuff:Ravenclaw:80:240   Gryffindor:Slytherin:200:310 
Ravenclaw:Gryffindor:80:180   Slytherin:Hufflepuff:50:160'''


def celkove_skore(zaznamy: str) -> Dict[str, int]:
    """
    >>> pprint(celkove_skore(PRIKLAD))
    {'Gryffindor': 580, 'Hufflepuff': 360, 'Ravenclaw': 500, 'Slytherin': 570}
    >>> pprint(celkove_skore(''))
    {}
    """
    
    vysledok = {}
    casti = zaznamy.split(" ")
    for i in range(len(casti)):
        zapas = casti[i].strip().split(':')
        
        if len(zapas) != 4:
            continue
        vysledok[zapas[0]] = vysledok.get(zapas[0], 0) + int(zapas[2])
        vysledok[zapas[1]] = vysledok.get(zapas[1], 0) + int(zapas[3])

        """
        if vysledok.get(zapas[0], -1) == -1:
            vysledok[zapas[0]] = 0

        if vysledok.get(zapas[1], -1) == -1:
            vysledok[zapas[1]] = 0

        vysledok[zapas[0]] += int(zapas[2])
        vysledok[zapas[1]] += int(zapas[3])
        """
        
    return vysledok


pprint(celkove_skore('''Gryffindor:Hufflepuff:200:120  Ravenclaw:Slytherin:180:210 
Hufflepuff:Ravenclaw:80:240   Gryffindor:Slytherin:200:310 
Ravenclaw:Gryffindor:80:180   Slytherin:Hufflepuff:50:160'''))
