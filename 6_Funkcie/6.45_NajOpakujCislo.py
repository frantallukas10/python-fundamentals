# Najčastejšie sa opakujúce číslo

# Napíšte definíciu funkcie najcastejsi, ktorá prijíma zoznam čísel a vracia najčastejšie sa opakujúce číslo v tomto zozname.

# Pokiaľ bude zoznam prázdny, vráťte None. Pokiaľ bude viac rôznych čísel s rovnakým, maximálnym počtom výskytov, vráťte jedno z nich - je jedno ktoré.

# Sample Input:
# [1, 2, 3, 3, 4, 4, 1, 2, 5, 3, 2, 1, 2]

# Sample Output:
# 2

from typing import List

def najcastejsi(cisla: List[int]) -> int:
    sort_cisla = sorted(cisla)
    if (len(sort_cisla) == 0):
        return None
    pole = []
    for cislo in sort_cisla:
        if cislo not in pole:
            pole.append(cislo) # [1, 2, 3, 4, 5]
    
    pocet = 0
    posledny_pocet = 0
    vysledok = 0
    for cisloI in range(0, len(pole)):
        for cisloJ in range(0, len(sort_cisla)):
            if (pole[cisloI] == sort_cisla[cisloJ]):
                pocet = pocet + 1
                if(pocet > posledny_pocet):
                    posledny_pocet = pocet
                    vysledok = pole[cisloI]
            else:
                pocet = 0
    return vysledok
                    
print(najcastejsi([1, 2, 3, 3, 4, 4, 1, 2, 5, 3, 2, 1, 2]))