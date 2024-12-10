# Precvičenie logických výrazov

# V premennej rok máme uložené prirodzené číslo. Napíšte program, ktorý zistí, či ak sa jedná o priestupný rok a uloží výsledok do premennej priestupný.

# Sample Input 1:
# 2012

# Sample Output 1:
# True

# Sample Input 2:
# 2015

# Sample Output 2:
# False

rok = int(input())

if (rok % 4 == 0):
    if(rok % 100 == 0):
        if(rok % 400 == 0):
            prestupny = True
        else:
            prestupny = False
    else:
        prestupny = True
else:
    prestupny = False

print(prestupny)