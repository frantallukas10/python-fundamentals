# KOSTKY

# Na vstupe získate prirodzené číslo. Nájdite všetky spôsoby, ako možno toto číslo získať pri hode dvoma hracími kockami.

# Výsledok vypíšte ako zoznam dvojíc. Dvojica vypisujte v tvare (menšie, väčšie) a zoraďte ich podľa prvého čísla. Pokiaľ zadané číslo nie je možné získať pri hode dvoma kockami, vráťte proste prázdny zoznam.

# Sample Input:
# 8

# Sample Output:
# [(2, 6), (3, 5), (4, 4)]

vstup = input()
vystup = ''
index = 0
for i in range(1, 7):
    for j in range(1, 7):
        if(i + j == int(vstup) and i <= j):
            if(index == 0):
                index += 1
                vystup = '(' + str(i) + ', ' + str(j) + ')'
            else:
                vystup += ', (' + str(i) + ', ' + str(j) + ')'
if(vystup != ''):
    print('[' + vystup + ']')