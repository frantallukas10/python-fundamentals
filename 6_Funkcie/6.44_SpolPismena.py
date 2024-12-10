# Společná písmena

# Napíšte definíciu funkcie spolecna_pismena, ktorá prijíma zoznam reťazcov. Funkcia vráti zoznam znakov, ktoré sa vyskytujú v každom z týchto reťazcov. Zoznam bude zoradený podľa abecedy. Pokiaľ bude funkcia volaná na prázdnom zozname, vráti prázdny zoznam.

# Sample Input:
# spolecna_pismena(['mrkva', 'krkavec', 'krabice'])

# Sample Output:
# ['e', 'k', 'r']

from typing import List

def spolecna_pismena(retazce: List[str]) -> List[str]:
    if(len(retazce) == 0):
        return retazce
    najkratsi_vstup = retazce[0]
    for i in range(0, len(retazce)):
        if(len(najkratsi_vstup) < len(retazce[0])):
            najkratsi_vstup = retazce[0]                  
    retazce.remove(najkratsi_vstup)
    pole_bez_najkratsieho_vstupu = retazce

    pole_nerovnakych_znakov = []
    for i in range(0, len(pole_bez_najkratsieho_vstupu)): 
        for j in range(0, len(najkratsi_vstup)):
            if (
                najkratsi_vstup[j] not in pole_bez_najkratsieho_vstupu[i] and
                najkratsi_vstup[j] not in pole_nerovnakych_znakov
            ):
                pole_nerovnakych_znakov.append(najkratsi_vstup[j])
    pole_rovnakych_znakov = []
    for i in range(0, len(najkratsi_vstup)):
        if(najkratsi_vstup[i] not in pole_nerovnakych_znakov):
            pole_rovnakych_znakov.append(najkratsi_vstup[i])
    vysledok = []
    for i in range(0, len(pole_rovnakych_znakov)):
        if (pole_rovnakych_znakov[i] not in vysledok):
            vysledok.append(pole_rovnakych_znakov[i])
    vysledok.sort()
    return vysledok
    
print(spolecna_pismena(['mrkva', 'krkavec', 'krabice']))