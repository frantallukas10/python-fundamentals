# Napíšte definíciu funkcie funkcia1, ktorá zoberie ako parameter zoznam kladných reálnych čísel - každé číslo predstavuje polomer kruhu. Funkcia vypíše na výstup polomer a obsah každého kruhu v nasledujúcom formáte:
#  Polomer | Obsah
#  0.25 | 0.20
#  1.20 | 4.52
#  100.00 | 31415.93

# (Každý stĺpec má šírku 8 znakov, medzi nimi je trojica znakov medzera-zvislou čiarou-medzera. Hodnoty sa vypisujú na 2 desatinné miesta zarovnané doprava. Obsah kruhu S = πrr2.)

from typing import Dict, List, Tuple
from pprint import pprint

import math

def funkcia1(polomery: List[float]) -> None:
    """Formátuj polomer a obsah kruhu.
    >>> funkcia1([100, 1.2, 0.25])
      Polomer |    Obsah
      100.00 | 31415.93
        1.20 |     4.52
        0.25 |     0.20
    """
    # 1. riešenie
    print(' Polomer |     Obsah')
    for cisla in range(0, len(polomery)):
        polomer = polomery[cisla]
        obsah = math.pi * polomer ** 2
        print(f'{polomer:>8.2f}'+ ' | ' + f' {obsah:>8.2f}')
    
    # Alternatívne riešenie:
    # print(' Polomer |    Obsah')
    # for r in polomery:
    #     S = math.pi * r**2
    #     print(f'{r:>8.2f} | {S:>8.2f}')
        
print(funkcia1([100, 1.2, 0.25]))
