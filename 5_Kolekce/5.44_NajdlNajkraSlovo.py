# Najdlhšia a najkratšiu slovo

# V zadanom vstupu nájdite najdlhšia a najkratšia slovo

# Sample Input:
# pes macka holub sliepka sokol anakonda slon liška

# Sample Output:
# anakonda
# pes

vstup = input().split(' ')
index = 0
for i in vstup:
    if(index == 0):
        hladane_najdlhsie_slovo = len(i)
        hladane_najkratsie_slovo = len(i)
        index += 1
    if (hladane_najdlhsie_slovo <= len(i)):
        hladane_najdlhsie_slovo = len(i)
        najdlhsie_slovo = i
    if(hladane_najkratsie_slovo >= len(i)):
        hladane_najkratsie_slovo = len(i)
        najkratsie_slovo = i

print(najdlhsie_slovo + '\n' + najkratsie_slovo)