# Vedecky format

# Vstupný reťazec preveďte na číslo a vypíšte ako číslo vo vedeckom formáte.

# Sample Input:
# 40800000000.00000000000000

# Sample Output:
# 4.08E+10

vstup_str = input() 
x = float(vstup_str)
print('{:^20.2E}'.format(x))