# Zoznam čísel

# Napíšte definíciu funkcie cisla, ktorá prijíma reťazec. Reťazec rozdeľte podľa ";" a prvky, ktoré nemožno previesť na číslo, ignorujte. Návratovú hodnotou funkcie bude zoznam čísel (float).

# Vaša funkcia bude volaná takto:

# retezec = input()
# print(cisla(retazec))

# Sample Input:
# 8;1;2.2;_;5.3;9.8

# Sample Output:
# [8.0, 1.0, 2.2, 5.3, 9.8]

from typing import List

def cisla(retazec: str) -> List[float]:
    retazec = retazec.split(';')
    zoznam = []
    for i in range(0,len(retazec)):
        try:
            vstup = float(retazec[i])
            zoznam.append(vstup)
        except ValueError:
            i = i + 1
    return zoznam

retazec = input()
print(cisla(retazec))
