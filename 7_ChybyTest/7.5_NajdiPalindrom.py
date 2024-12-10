# Najdi palindrom

# Napíšte definíciu funkcie najdi_palindrom, ktorá berie parametre veta a n. Funkcia vo vete nájde palindróm dĺžky n a vráti ho ako návratovú hodnotu. Ak sa vo vete žiadny takýto palindróm nenachádza, funkcia vyhodí chybu typu LookupError. (Funkcia bude ignorovať veľkosť písmen a medzery.)

# Sample Input 1:
# 'Petr jede v kajaku', 5

# Sample Output 1:
# 'kajak'

# Sample Input 2:
# 'Kuna nanuk nemá ráda', 9

# Sample Output 2:
# 'kunananuk'

# Sample Input 3:
# 'Milujem Python', 3

# Sample Output 3:
# LookupError

def najdi_palindrom(veta: str, n: int) -> str:
    pole = veta.split()
    slovo = ''
    vysledok = False
    for index in range(0, len(pole)):
        slovo = slovo + pole[index]
    slovo2 = ''
    for i in range(0, len(slovo)):
        slovo2 = slovo[(i+1-n):(i+1)]
        if(len(slovo2) == n):
            if (slovo2.lower() == slovo2[::-1].lower()):
                vysledok = slovo2.lower()
    if(vysledok == False):
        raise LookupError()
    return vysledok

print(najdi_palindrom('Kuna nanuk nemá ráda', 9))