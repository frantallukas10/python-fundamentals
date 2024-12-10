# Najkratšia a najdlhšia

# Napíšte definíciu funkcie kratke_dlhe, ktoré prijmú reťazec. Výstupom funkcie bude n-tice obsahujúce dve slová, najkratšia slovo a najdlhšia slovo. Vstup nebude obsahovať interpunkciu.

# Sample Input:
# kratke_dlhe('Moja najobľúbenejšia hračka bol plyšový medvedík Pú')

# Sample Output:
# ('Pú', 'najobľúbenejšia')

from typing import Tuple

def kratke_dlhe(retazec: str) -> Tuple[str, str]:
    vstupy = retazec.split()
    dlhe = vstupy[0]
    kratke = vstupy[0]
    dlzka_vstupy = 0
    for i in range(0, len(vstupy)):
        dlzka_vstupy = len(vstupy[i])
        if(dlzka_vstupy > len(dlhe)):
            dlhe = vstupy[i]
        if(dlzka_vstupy < len(kratke)):
            kratke = vstupy[i]
    return (kratke, dlhe)
    
print(kratke_dlhe('Moja najobľúbenejšia hračka bol plyšový medvedík Pú'))