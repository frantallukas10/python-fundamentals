# Súčet a súčin

# Napíšte definíciu funkcie sucet_a_sucin, ktorá ako argument dostane zoznam čísel a vráti ich súčet a súčin.

# Ďalej doplňte kód, ktorý zo vstupu načíta riadok s reálnymi číslami, zavolá funkciu sucet_a_sucin a vypíše ich súčet a súčin (formát pozri Sample Output).

# Sample Input:
# 1.5 2.0 4.0

# Sample Output:
# Súčet:    7.50
# Súčin:   12.00

from typing import List, Tuple
import math

def sucet_a_sucin(cisla: List[float]) -> Tuple[float, float]:
    """
    >>> sucet_a_sucin([1.5, 2.0, 4.0])
    (7.5, 12.0)
    >>> sucet_a_sucin([0.25, 10.5, 0.75, -2.0, 2.0])
    (11.5, -7.875)
    """
    sucet = sum(cisla)
    sucin = 1
    for i in cisla:
      sucin = sucin * i
    return(f'Súčet: {sucet:>7.2f} \nSúčin: {sucin:>7.2f}')

print(sucet_a_sucin([1.5, 2.0, 4.0]))