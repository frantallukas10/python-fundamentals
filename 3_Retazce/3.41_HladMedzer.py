# Hladam medzeru

# V zadanom texte najdite prvý výskyt medzery a tri znaky, ktoré za ňou následujú.

# Sample Input:
# Zajtra bude krásne počasie.

# Sample Output:
# 6
# bud

string = input()
medzera_index = string.find(' ')
print(medzera_index)
print(string[1+medzera_index:4+medzera_index]) # rozsah [od:do]
