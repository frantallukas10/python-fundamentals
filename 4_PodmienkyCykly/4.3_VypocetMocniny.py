# Mocniny

# Zo vstupu získajte dve čísla a spočítajte mocninu. Prvé číslo (float) je základ, druhé číslo (int) je exponent.
# Úlohu riešte pomocou cyklu, bez použitia operátora ** alebo funkcie pow.

# Sample Input:
# 2 3

# Sample Output:
# 8

vstup = input()
zaklad, exponent = vstup.split()
n = 1

for i in range(1, int(exponent) + 1):
    n = n * float(zaklad)
print(int(n))

#--------------------------------------
# z, e = input().split()
# z = int(z)
# e = int(e)
# result = 1
# for i in range(e):
#     result *= z
# print(result)