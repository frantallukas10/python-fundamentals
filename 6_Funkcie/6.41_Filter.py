# Filter

# Napíšte definíciu funkcie nasobky3, ktorá prijíma zoznam celých čísel. Návratovú hodnotou funkcie bude prefiltrovaný zoznam čísel, ktoré sú deliteľné 3 bezo zvyšku.

# Sample Input:
# nasobky3([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# Sample Output:
# [3, 6, 9, 12]

from typing import List

def nasobky3(cisla: List[int]) -> List[int]: 
    vysledok = []
    for i in range(0,len(cisla)):
        if(cisla[i] % 3 == 0):
            vysledok.append(cisla[i])
    return vysledok
        
print(nasobky3([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))