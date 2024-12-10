# Filter 2

# Napíšte definíciu funkcie moj_filter, ktorá prijíma zoznam čísel (môžu byť int i float). Funkcia bude vracať trojicu obsahujúce minimum, maximum a zoznam so zvyšnými číslami. 

# Sample Input:
# moj_filter([15, 10, 5, 20, 25.2])

# Sample Output:
# (5, 25.2, [15, 10, 20])

def moj_filter(cisla: list) -> tuple:
    mini = cisla[0]
    maxi  = cisla[0]
    zvysok = []
    for cislo in range(0, len(cisla)):
        if (cisla[cislo] > maxi):
            maxi = cisla[cislo]
        if (cisla[cislo] < mini):
            mini = cisla[cislo]
    for cislo in range(0, len(cisla)):
        if (cisla[cislo] != maxi and cisla[cislo] != mini):
            zvysok.append(cisla[cislo])
    return (mini, maxi, zvysok)
    
print(moj_filter([15, 10, 5, 20, 25.2]))  