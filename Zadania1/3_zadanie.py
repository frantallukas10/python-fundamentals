# Sekvencia DNA sa skladá zo štyroch typov nukleových báz (A, C, G, T). Relatívna početnosť bázy vyjadruje, aká časť sekvencie je tvorená daným typom bázy (počet výskytov bázy / dĺžka sekvencie). Súčet relatívnej početnosti je teda vždy rovna 1.
# Napíšte definíciu funkcie funkcia3, ktorá zoberie ako parameter sekvenciu DNA a vráti slovník s relatívnou početnosťou nukleových báz. (Poznámka: funkcia pprint v doctestu vypisuje obsah slovníka zoradenu podľa kľúčov, poradie teda nemusíte riešiť. Hodnoty nie je potreba nijak zaokrúhľovať.)

from typing import Dict, List, Tuple
from pprint import pprint

import math

def funkcia3(sekvencia: str) -> Dict[str, float]:
    """Spočítaj relativnu četnosť baz v sekvencii DNA.
    >>> pprint(funkcia3('ACGTTTTGAG'))
    {'A': 0.2, 'C': 0.1, 'G': 0.3, 'T': 0.4}
    >>> pprint(funkcia3('AAA'))
    {'A': 1.0, 'C': 0.0, 'G': 0.0, 'T': 0.0}
    """
    dlzka = len(sekvencia)
    relativna_cetnost = {baza: sekvencia.count(baza) / dlzka for baza in 'ATGC'}
    return relativna_cetnost
    
    # # Alternatívne riešenie:
    # cetnost = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    # for baza in sekvencia:
    #     cetnost[baza] += 1
    # dlzka = len(sekvencia)
    # for baza in cetnost:
    #     cetnost[baza] /= dlzka
    # return cetnost

print(funkcia3('ACGTTTTGAG'))