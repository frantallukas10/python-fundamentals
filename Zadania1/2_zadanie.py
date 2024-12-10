# Napíšte definíciu funkcie funkcia2, ktorá zoberie ako parameter zoznam celých čísel. Návratovú hodnotou funkcie bude prefiltrovaný zoznam obsahujúci iba čísla deliteľné tromi alebo piatimi.

from typing import Dict, List, Tuple
from pprint import pprint

import math

def funkcia2(cisla: List[int]) -> List[int]:
    """Vyfiltruj iba čísla delitelné 3 alebo 5.
    >>> funkcia2([7, 12, 35, 15, 45, 16, 18])
    [12, 35, 15, 45, 18]
    """
    # 1. riešenie
    vysledok = []
    for i in range(0,len(cisla)):
        if(cisla[i] % 3 == 0) or (cisla[i] % 5 == 0):
            vysledok.append(cisla[i])
    return vysledok

    # # Alternatívne riešenie:
    # vysledek = []
    # for cislo in cisla:
    #     if cislo % 3 == 0 or cislo % 5 == 0:
    #         vysledek.append(cislo)
    # return vysledek

    # # Alternatívne riešenie:
    # return [x for x in cisla if x%3 == 0 or x%5 == 0]

print(funkcia2([7, 12, 35, 15, 45, 16, 18]))