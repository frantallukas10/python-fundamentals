"""
Úloha:
Alica hádže kockou 10x. Aká je šanca, že z týchto 10 hodov padnú aspoň 4 šestky?
Úlohu riešte pomocou simulácie, tj. Náhodne vygenerujte 10 hodov kockou (modul random) a rozhodnite, či padli aspoň 4 šestky. Toto opakujte 10000 krát a spočítajte, aké percento pokusov bolo úspešné.
(Správny výsledok je okolo 7%, samozrejme to vždy vyjde trochu inak.)

Bonus:
Bob hádže kockou 100x. Aká je šanca, že sa mu v rámci týchto 100 hodov podarí hodiť 4 šestky PO SEBE?
(Správny výsledok je okolo 6%).
"""

import random
import math


def simuluj_4x6(n_hodov: int) -> bool:
    """Simulujte n_hodov hodov kockou a vráť True, ak padli aspoň 4 šestky."""
    hody = [random.randint(1, 6) for i in range(n_hodov)]
    return hody.count(6) >= 4

def simuluj_4x6_po_sebe(n_hodov: int) -> bool:
    """Simulujte n_hodov hodov kockou a vráť True, ak padli aspoň 4 šestky po sebe."""
    hody = [random.randint(1, 6) for i in range(n_hodov)]
    hody_retezec = ''.join(str(x) for x in hody)
    return '6666' in hody_retezec

n_pokusov = 10000
uspesnych_Alica = 0
uspesnych_Bob = 0

for i in range(n_pokusov):
    if simuluj_4x6(10):
        uspesnych_Alica += 1

pravdepodobnost_Alica = uspesnych_Alica / n_pokusov
pravdepodobnostPercenta_Alica = pravdepodobnost_Alica * 100

for i in range(n_pokusov):
    if simuluj_4x6_po_sebe(100):
        uspesnych_Bob += 1

pravdepodobnost_Bob = uspesnych_Bob / n_pokusov
pravdepodobnostPercenta_Bob = pravdepodobnost_Bob * 100

print(f'Pravdepodobnost je cca - Alica: {pravdepodobnostPercenta_Alica:.2f} % ')
print(f'Pravdepodobnost je cca - Bob: {pravdepodobnostPercenta_Bob:.2f} % ')
