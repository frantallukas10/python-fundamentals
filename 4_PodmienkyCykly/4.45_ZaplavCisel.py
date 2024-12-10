# Záplava čísel

# Na vstupe získate reťazec obsahujúci iba číslice. Vypíšte na výstup reťazec, ktorý bude obsahovať každú číslicu zo vstupu toľko krát, koľko je hodnota číslice (tj. Dve dvojky, päť pätiek atď ...).

# Sample Input:
# 25104

# Sample Output:
# 225555514444

vstup = input()
for i in vstup:
    print(int(i) * i, end= '')