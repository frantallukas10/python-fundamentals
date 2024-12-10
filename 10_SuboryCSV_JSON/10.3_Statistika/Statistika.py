"""
Úloha:
Napíšte program, ktorý načíta súbor vo formáte CSV, spočíta štatistiku z každého stĺpce a výsledok uloží do výstupného CSV súboru.
Užívateľ zadá názov vstupného a výstupného súboru z príkazového riadku.
Ďalej môže užívateľ zadať:
- že prvý riadok tabuľky vo vstupnom súbore sa má brať ako hlavička a táto hlavička sa má vypísať aj do výstupného súboru (pomocou --header)
- aký je oddeľovač vo vstupnom a výstupnom súboru (pomocou --delimiter)
- aký typ štatistiky (priemer / medián / min / max) sa má počítať (pomocou --stat)

Ak sa niektoré hodnoty v stĺpci nepodarí previesť na číslo, nechajte
bunku zodpovedajúc tomuto stĺpci vo výstupnej tabuľke prázdnu.

Príklady spustenie z príkazového riadku:
$ python  Statistika.py  tabulka1.csv  vystup1.csv  --stat median  --header  --delimiter ";"
$ python  Statistika.py  tabulka2.csv  vystup2.csv  --stat max

(Všimnite si, že znak bodkočiarku musí byť v úvodzovkách. To preto, že niektoré znaky (; | < >? * Medzera atď.) sú špeciálne znaky príkazového riadku (tj. Bash alebo PowerShellu). Aby sa ich špeciálne funkcie zrušila, zadáme ich do príkazového riadku v úvodzovkách. Tieto úvodzovky sa automaticky odstránia, tj. ak zadáme napr. ";", tak Python dostane už len jeden znak - bodkočiarka.)

Vzorové výstupne subory su vystup1-vzor.csv, vystup2-vzor.csv.
"""

import argparse
import csv
from typing import List, Optional
import statistics


def nacitaj_argumenty():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Input CSV file', type=str)
    parser.add_argument('output', help='Output CSV file', type=str)
    parser.add_argument('-H', '--header', help='Interpret the first line as column names', action='store_true')
    parser.add_argument('-d', '--delimiter', help='Delimiter in the CSV files', type=str, default=',')
    parser.add_argument('-s', '--stat', help='Type of statistic to be computed', choices=['mean', 'median', 'min', 'max'], default='mean')
    arguments = parser.parse_args()
    return arguments


def extrahuj_stlpec(tabulka: List[List[str]]) -> List[List[float]]:
    """
    Prerob tabuľku zo zoznamu riadkov na zoznam stĺpcov a konvertujte hodnoty na float.
    Ak niektoré hodnoty v stĺpci nemožno previesť na float, vlož miesto
    tohto stĺpca [].
    """
    n_stlpcov = len(tabulka[0])
    stlpec = []
    for i in range(n_stlpcov):
        try:
            novy_stlpce = [float(radek[i]) for radek in tabulka]
        except ValueError:  # Ak sa niektorú hodnotu nepodarí konvertovať na float
            novy_stlpce = []
        stlpec.append(novy_stlpce)
    return stlpec


def spocitaj_statistiku(typ_statistiky: str, hodnoty: List[float]) -> Optional[float]:  # Optional[float] znamená float alebo None
    """
    Spočítaj požadovanu statistiku (mean/median/max/min) pre zaznam hodnot. Vrať None, pokial je zoznam prázdný.
    """
    if len(hodnoty) == 0:
        return None
    elif typ_statistiky == 'mean':
        return statistics.mean(hodnoty)
    elif typ_statistiky == 'median':
        return statistics.median(hodnoty)
    elif typ_statistiky == 'min':
        return min(hodnoty)
    elif typ_statistiky == 'max':
        return max(hodnoty)
    else:
        raise ValueError(f'Neznámi typ statistiky: {typ_statistiky}')


args = nacitaj_argumenty()

with open(args.input, encoding='utf8') as f:
    reader = csv.reader(f, delimiter=args.delimiter)
    tabulka = list(reader)
        
if args.header:
    hlavicka, *tabulka = tabulka

stlpec = extrahuj_stlpec(tabulka)

statistiky = []
for stlpce in stlpec:
    statistika = spocitaj_statistiku(args.stat, stlpce)
    statistiky.append(statistika)

with open(args.output, 'w', encoding='utf8') as f:
    writer = csv.writer(f, delimiter = args.delimiter)
    if args.header:
        writer.writerow(hlavicka)
    writer.writerow(statistiky)
