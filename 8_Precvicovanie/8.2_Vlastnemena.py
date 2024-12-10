# Vlastné mená

# Napíšte definíciu funkcie vlastne_mena, ktorá ako argument prijme zoznam reťazcov a vyberie iba tie, ktoré sa začínajú veľkým písmenom. Vyhovujúce reťazca vráti opäť ako zoznam.

from typing import List

def vlastne_mena(zoznam: List[str]) -> List[str]:
    """
    >>> vlastne_mena(['pes', 'Rex', 'Bohunice', 'sklenica', 'sliepka'])
    ['Rex', 'Bohunice']
    """
    vystup = []
    for slovo in zoznam:
      if slovo[0].isupper(): # ak je velke pismeno
        vystup.append(slovo)
    return vystup

print(vlastne_mena(['pes', 'Rex', 'Bohunice', 'sklenica', 'sliepka']))