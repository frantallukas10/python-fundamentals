"""
Úloha:
Vytvorte program, ktorý načíta súbor CSFD-Hleda_se_Nemo.txt a vypíše na výstup všetky riadky, na ktorých sa vyskytuje slovo Nemo. Navyše bude u každého riadku uvedené poradie riadku v pôvodnom súbore.
Pozor: vyberte správne kódovanie, aby sa podarilo súbor načítať a aby sa správne zobrazila diakritika.

Vzorový výstup:  
   2 a odlehlém příbytku ze sasanek Marlin a jeho jediný syn Nemo. Marlin se s
   4 snaží svého syna před nástrahami okolí ochránit. Nemo je však, stejně jako
  23 postaviček. Scénáristou a režisérem filmu Hledá se Nemo je Andrew Stanton,
  27 Hledá se Nemo a jeho úžasný podmořský svět je zcela novým uměleckým a
"""

subor = 'CSFD-Hleda_se_Nemo.txt'
hladane_slovo = 'Nemo'

with open(subor, encoding='cp1250') as f: # f = moj nazov pre otvoreny subor
    for i, riadok in enumerate(f, 1): # funckia ocisluje prvky a zacina od 1
        if hladane_slovo in riadok:
            print(f'{i:>4} {riadok.strip()}')
