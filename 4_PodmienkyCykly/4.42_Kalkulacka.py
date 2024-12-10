# Kalkulačka

# Na vstupe získate dve desatinné čísla oddelené matematickým operátorom. Vykonajte výpočet a vypíšte výsledok zaokrúhlený na 2 desatinné miesta.

# Možné operácie:

# Sčítanie +
# Odčítanie -
# Násobenie *
# Delenie /
# Ak bude zadaný nepovolený operátor, vypíšte na výstupe None.

# Sample Input:
# 1 + 2

# Sample Output:
# 3.00

cislo_1, znamienko, cislo_2 = input().split()
if znamienko == '+':
    riesenie = float(cislo_1) + float(cislo_2)
    print('{:.2f}'.format(riesenie))
elif znamienko == '-':
    riesenie = float(cislo_1) - float(cislo_2)
    print('{:.2f}'.format(riesenie))
elif znamienko == '/':
    riesenie = float(cislo_1) / float(cislo_2)
    print('{:.2f}'.format(riesenie))
elif znamienko == '*':
    riesenie = float(cislo_1) * float(cislo_2)
    print('{:.2f}'.format(riesenie))
else:
    print('None')