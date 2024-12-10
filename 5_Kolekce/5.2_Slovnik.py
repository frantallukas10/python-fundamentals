# Uprava podla kluca

# Na vstupe získate názov farieb a ich počítačovú reprezentáciu na preskáčku. Vaším cieľom je vytvoriť slovník, ktorý bude ako kľúč obsahovať názov farby a ako hodnotu jej reprezentáciu. Vypíšte celý slovník

# Sample Input:
# červená #FF0000 modrá #0000FF zelená #008000 žlutá #FFFF00

# Sample Output:
#  {'červená': '#FF0000', 'modrá': '#0000FF', 'zelená': '#008000', 'žlutá': '#FFFF00'}

vstup = input().split( )
vystup = set()
farba = ''
for i in range(len(vstup)):
    if(i % 2 == 0):
        farba += "'" + str(vstup[i]) + "': "
    else:
        if(i == len(vstup) - 1):
            farba += "'" + str(vstup[i]) + "'"
        else:
            farba += "'" + str(vstup[i]) + "', "

print('{' + farba + '}')

# # Alternatívne riešenie:
# casti = input().split()
# farby = casti[0::2]
# kody = casti[1::2]
# slovnik = {}
# for farba, kod in zip(farby, kody):
#     slovnik[farba] = kod
# print(slovnik)

# # Alternatívne riešenie: 
# casti = input().split()
# farby = casti[0::2]
# kody = casti[1::2]
# slovnik = {farba: kod for farba, kod in zip(farby, kody)}
# print(slovnik)

# # Alternativní řešení 2:
# casti = input().split()
# slovnik = {}
# for i in range(0, len(casti), 2):  # iterujeme ob 1
#     farba = casti[i]
#     kod = casti[i+1]
#     slovnik[farba] = kod
# print(slovnik)
