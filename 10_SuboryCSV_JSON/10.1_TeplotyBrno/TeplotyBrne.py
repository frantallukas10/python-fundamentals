"""
Úloha:
Vytvorte program, ktorý načíta CSV súbor Brno_denne_teploty.csv.
Následne spočíta priemernú teplotu pre každý mesiac v rokoch 1961-2017.
Výsledné priemerné hodnoty uložia do súboru Brno_mesacne_teploty.csv, a to tak, že každý riadok bude zodpovedať jednému roku a každý stĺpec jednému mesiaci v roku. Vzorový výsledok nájdete v Brno_mesacne_teploty-vzor.csv
Zdroj dat: http://portal.chmi.cz/historicka-data/pocasi/denni-data

Vystup v terminaly:
01:  -5.14
02:   1.59
03:   8.32
04:   9.19
05:  15.98
06:  21.02
07:  21.21
08:  22.08
09:  14.10
10:  10.63
11:   4.65
12:   1.87

Bonus: 
Upravte program tak, aby prijímal názov vstupného a výstupného súboru ako argumenty z príkazového riadku (hint: využite modul argparse).
"""

import csv

with open('Brno_denne_teploty.csv') as f:
    for i in range(4):  # Ignorujeme hlavičku (prve 4 riadky)
        f.readline()
    temperatures_by_years = {}
    for row in csv.reader(f):
        year = row[0]
        month = row[1]
        temperatures = [float(field) for field in row[2:] if field != '']
        average = sum(temperatures) / len(temperatures)
        if int(year) == 2017:
            print(f'{month}: {average:6.2f}')
        if year not in temperatures_by_years:
            temperatures_by_years[year] = []
        temperatures_by_years[year].append(average)

with open('Brno_mesacne_teploty.csv', 'w') as g:
    csv_writer = csv.writer(g)
    header = [''] + list(range(1, 13))
    csv_writer.writerow(header)
    for year, temperatures in temperatures_by_years.items():
        row = [year] + [f'{temp:.1f}' for temp in temperatures]
        csv_writer.writerow(row)
    