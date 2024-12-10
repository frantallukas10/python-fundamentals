# Scitavanie cisel

# Vytvorte program, ktorý bude od užívateľa načítavať reálne čísla, vždy iba jedno číslo na každom riadku. Keď používateľ napíše do riadku "stop", vypíše sa súčet doteraz zadaných čísel a program skončí. Súčet vypisujte na 2 desatinné miesta.

# Sample Input:
# 5
# 1.2
# 0.5
# stop

# Sample Output:
# 6.70

y = 0
while True:
    x = str(input())
    if (x == 'stop'):
        break
    y = float(y) + float(x)

print('{:.2f}'.format(y))

# #Alternatívne riešenie:
# suma = 0
# vstup = input()
# while vstup != 'stop':
#     x = float(vstup)
#     suma += x
#     vstup = input()
# print(f'{suma:.2f}')


# #Alternatívne riešenie:
# suma = 0
# while True:
#     vstup = input()
#     if vstup == 'stop':
#         print(f'{suma:.2f}')
#         break
#     else:
#         x = float(vstup)
#         suma += x
