# Hlada sa pozicia navacsie cisla

# Na vstupe získate jednotlivé čísla oddelené medzerou, vašou úlohou je nájsť pozíciu (index) najväčšieho čísla. Pokiaľ bude viac najväčších čísel, vráťte pozíciu prvého.

# Vyskúšajte tiež:
# 1 1 1 1 1
# nebo
# 2 3 4 5 1

# Sample Input:
# 1 2 3 4 5 10 7 8

# Sample Output:
# 5


vstup = input().split()
dlzka = len(vstup)

for i in range(0, dlzka):
    vstup[i] = int(vstup[i])
    
maxi = max(vstup) # maximalne cislo
if vstup.count(int(maxi)) > 1:
    print(vstup.index(int(maxi)))
else:
    print(vstup.index(int(maxi)))

# # Alternatívne riešenie:
# retezce = input().split()
# cisla = [int(r) for r in retezce]
# maximum = max(cisla)
# index_maxima = cisla.index(maximum)
# print(index_maxima)
