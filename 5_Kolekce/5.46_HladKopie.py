# Hledame kopie

# Na vstupe získate niekoľko slov, z ktorých dve sú rovnaké. Vypíšte, o ktore slovo sa jedná a na ktorých dvoch pozíciách sa nachádza (pozícia počítame od nuly).

# Hint: Ide to aj bez použitia funkcií ako find alebo index. Stačí využiť vhodný typ kolekcie.

# Sample Input:
# košík bunda kokos olovo mango kokos užovka karate

# Sample Output:
# kokos 2 5

vstup = input()
pole = vstup.split( )
for i in range(len(pole)):
    if(str(pole[i]) in str(pole[i + 1:len(pole)]) or str(pole[i]) in str(pole[0: i])):
        hladane_slovo = pole[i]
    if(str(pole[i]) in str(pole[i + 1:len(pole)])):
        pozicia_prve_slovo = i
    if(str(pole[i]) in str(pole[0: i])):
        pozicia_druho_slovo = i
print(hladane_slovo, pozicia_prve_slovo, pozicia_druho_slovo)