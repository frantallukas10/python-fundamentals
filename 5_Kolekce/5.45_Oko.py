# Oko

# V hre Oko (Blackjack) je cieľom získať čo najväčší počet bodov, nie však viac ako 21. Pritom karty 2 až 10 majú pri svoju vlastnú hodnotu; karty J, Q, K (spodok, kráľovná, kráľ) majú hodnotu 10; eso (A) má hodnotu 11.

# Napr. ak mám na ruke karty 3, 5, K, 2, potom mám 3 + 5 + 10 + 2 = 20 bodov. Ak mám na ruke karty 6, J, A, potom mám 0 bodov, pretože 6 + 10 + 11 = 27, čo je viac ako 21.

# Na vstupe získate postupnosť kariet oddelených čiarkami. Spočítajte, za koľko bodov sa tieto karty počítajú, a výsledok vypíšte na výstup.

# input: 2, 3, 5, K
# output: 20

# input: 6, J, A
# output: 0

vstup = input().split(', ')
vysledok = 0
for i in vstup:
    if(str(i) == 'J' or str(i) == 'Q' or str(i) == 'K'):
        i = 10
    if(str(i) == 'A'):
        i = 11
    vysledok += int(i)
    
if(vysledok <= 21):
    print(vysledok)
else:
    print(0)
