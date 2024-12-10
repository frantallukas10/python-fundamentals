# Najmenší spoločný násobok

# Pre dve zadané čísla nájdite najmenší spoločný násobok v rozsahu 1-100 a ten vypíšte. Pokiaľ toto číslo nenájdete, vypíšte len None.
# -----------------------------------------------------------
# NSN(16,6):
# rozklad 16: 16 = 2×8 = 2×2×4 = 2^4
# Rozklad 6: 6 = 2×3
# NSN(16,6) = 2^4 × 3 = 48

# Ak m je deliteľné n, potom najmenší spoločný násobok je m.
# Ak m a n sú nesúdeliteľné, najmenší spoločný násobok je ich súčin.
# Súčin najmenšieho spoločného násobku a najväčšieho spoločného deliteľa čísel m a n je ich súčin.

# Vyskúšajte tiež:
# 12 15
# 3 6
# 8 11
# 8 21 

# Sample Input:
# 4 6

# Sample Output:
# 12

vstup_1, vstup_2 = input().split()
if int(vstup_1) > int(vstup_2):
    vacsi_vstup = int(vstup_1)
else:
    vacsi_vstup = int(vstup_2)
while True:
    if(vacsi_vstup % int(vstup_1) == 0) and (vacsi_vstup % int(vstup_2) == 0):
        vysledok = vacsi_vstup
        break
    vacsi_vstup += 1
    
if 0 < vysledok and vysledok <= 100:
    print(vysledok)
else:
    print(None)