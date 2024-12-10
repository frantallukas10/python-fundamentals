# Caesarova šifra

# Na vstupe získate číslo a správu. Táto správa je posunutá o počet znakov podľa zadaného čísla. Správu dekódujte a vypíšte. Medzery medzi znakmi ignorujte.

# Pomoc:
# Funkcia print s parametrom end nezalamuje výstup na nové riadky. Použite funcia chr a ord.

# Sample Input:
# 5#Rfrf rjqj rfxt

# Sample Output:
# Mama mele maso

posun, sprava = input().split("#")
for i in sprava:
    if ord(i) == 32: # lebo (space)
        sifrovanie = int(ord(i))
    else:
        sifrovanie = int(ord(i) - int(posun))
    print(chr(sifrovanie), end = '')
