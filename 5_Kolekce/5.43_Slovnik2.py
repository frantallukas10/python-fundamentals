# slovnik

#Na vstupe získate kľuče# hodnoty, vytvorte slovník a vyberte hodnotu pre kľúč utorok.

# Sample Input:
# pondelok#rizka utorok#smazak streda#halusky stvrtok#gulas piatok#smazak

# Sample Output:
# smazak

vstup = input().split(' ')
for i in vstup:
    if('utorok' in i):
        vstup = i.split('#')
        for j in vstup:
            if('utorok' not in j):
                print(j)

