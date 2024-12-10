# Mocniny

# Pre zadané čísla spočítjte druhe mocniny a vypíšte ich.

# Sample Input:
# 1 2 3 4 5 6

# Sample Output:
# 1 4 9 16 25 36

vstup = input().split()
for i in range(0, len(vstup)):
    vstup[i] = int(vstup[i])
    vystup = vstup[i]**2
    print(vystup, end= ' ')

