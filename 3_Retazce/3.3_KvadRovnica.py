# Kvadraticka rovnica

# Tak a teraz napíšte znova kód, ktorý bude riešiť korene kvadratickej rovnice, ale premenné a, b, c získajte zo štandardného vstupu a výsledok vypíšte na štandardný výstup. Čísla oddeľujte medzerou.

vstup = input()
a, b, c = vstup.split()

D = float(b)**2 - 4*float(a)*float(c)
x1 = (-float(b) + D**0.5)/(2*float(a))
x2 = (-float(b) - D**0.5)/(2*float(a))
print(float(x1), float(x2))


# vstupne hodnoty napr. 1.0 -5.0 6.0
# vystup: 3.0 2.03
# inak
#-----------------------------------------
# import math
# vstup = input()
# a, b, c = vstup.split()

# D = b**2 - 4*a*c
# x1 = (-b + math.sqrt(D)) / (2*a)
# x2 = (-b - math.sqrt(D)) / (2*a)
# print(float(x1), float(x2))
