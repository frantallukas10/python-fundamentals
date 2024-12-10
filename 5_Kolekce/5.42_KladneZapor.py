# Nepárne a párne

# Na vstupe získate čísla, tie rozdeľte na párne a nepárne. Najprv vypíšte nepárne, potom párne.

# Sample Input:
# 8 11 4 3 7 2 6 13 5 12

# Sample Output:
# 11 3 7 13 5
# 8 4 2 6 12

vstup = input().split()
vstup = [int(x) for x in vstup]
sude = ''
liche = ''
for i in range(len(vstup)):
    if(vstup[i] % 2 != 0):
        if(i == 0):
            sude += str(vstup[i])
        else:
            sude += ' ' + str(vstup[i])
    else:
        if(len(vstup) == i):
            liche += str(vstup[i])
        else:
            liche += str(vstup[i]) + ' '
print(sude + '\n' + liche)