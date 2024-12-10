# Bezpečný priemer

# Napíšte funkciu priemer, ktorá berie ako parameter zoznam reálnych čísel a vracia ich priemer (pomocou klasického vzorca suma / počet).

# Zamyslite sa nad tým, aké problémy by mohli počas výpočtu nastať, a napíšte funkciu tak, aby neskončila chybou. Ak sa priemer nedá spočítať, vráťte hodnotu math.nan (nan = not a number).

# Sample Input:
# [2, 7, 9]

# Sample Output:
# 6.000

import math
from typing import List

def priemer(cisla: List[float]) -> float:
    try:
        priemer = sum(cisla) / len(cisla)
        return priemer
    except (ZeroDivisionError, TypeError):
        return math.nan

cisla = input()
print(priemer(cisla))