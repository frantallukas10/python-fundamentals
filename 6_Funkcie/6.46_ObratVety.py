# Obratenie vety

# Napíšte funkciu veta_naopak, ktorá berie ako argument vetu a vráti túto vetu s všetkými slovami pospiatky. K tomu si napíšte pomocnú funkciu slovo_odzadu, ktorá berie iba jedno slovo a to vráti pospiatky. (Veľkosť písmen a interpunkciu neriešte.)

# Sample Input:
# veta_naopak('toto je tajná správa')

# Sample Output:
# otot ej ánjat avárps

def veta_naopak(veta: str) -> str:
    pole = veta.split()
    dlzka_pola = len(pole)
    vysledok = ''
    for i in range(0, dlzka_pola):
        vysledok = slovo_odzadu(pole[dlzka_pola - i - 1]) + ' ' + vysledok
    return vysledok

def slovo_odzadu(slovo: str) -> str:
    return ''.join(reversed(slovo)) # spojuje prvky pomocou ''

print(veta_naopak('toto je tajná správa'))