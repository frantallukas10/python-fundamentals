# Napíšte definíciu funkcie funkcia5, ktorá zoberie ako parameter reťazec obsahujúci celé čísla oddelené medzerami. Funkcia vráti:
# • reťazec '+', ak je viac kladných ako záporných čísel
# • reťazec '-', ak je viac záporných ako kladných čísel
# • reťazec '?', Ak je rovnaký počet kladných a záporných čísel.

from typing import Dict, List, Tuple

def funkcia5(cisla: str) -> str:
    """Zisti, či reťazec obsahuje viac kladných alebo záporných čísel.
    >>> funkcia5('5 10 -3 8 -1 0')
    '+'
    >>> funkcia5('-555')
    '-'
    >>> funkcia5('100 -8')
    '?'
    """
    zoznam = [int(s) for s in cisla.split()]
    kladnych = zapornych = 0
    for x in zoznam:
        if x > 0:
            kladnych += 1
        elif x < 0:
            zapornych += 1
    if kladnych > zapornych:
        return '+'
    elif kladnych < zapornych:
        return '-'
    else:
        return '?'

    # # Alternatívne riešenie:
    # zoznam = [int(s) for s in cisla.split()]
    # kladnych = sum(1 for x in zoznam if x > 0)
    # zapornych = sum(1 for x in zoznam if x < 0)
    # if kladnych > zapornych:
    #     return '+'
    # elif kladnych < zapornych:
    #     return '-'
    # else:
    #     return '?'

print(funkcia5('5 10 -3 8 -1 0'))