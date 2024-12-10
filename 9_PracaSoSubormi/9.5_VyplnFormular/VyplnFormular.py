"""
Úloha:
Vytvorte program, ktorý bude načítať súbor formular.txt a postupne ho vypisovať na štandardný výstup. Na každom riadku končiacom dvojbodkou sa výpis zastaví a od užívateľa (tj. Zo štandardného vstupu) sa načíta potrebný údaj. Formulár s doplnenými údajmi sa uložia do súboru formular-vyplneny.txt.

Bonus: 
Modifikujte program tak, aby umožnil užívateľovi zadať názov
vstupného a výstupného súboru. Ak výstupný súbor už existuje, spýta sa
program užívateľa, či chce tento súbor prepísať.

Bonus2: 
Na koniec vytvoreného súboru doplňte automaticky dátum vyplnenia.
"""
from os import path # bonus
import datetime # bonus2

vstupny_subor = input('Vstupny subor: ')
vystupny_subor = input('Vystupny subor: ')

if path.exists(vystupny_subor): # ak existuje tento subor potom... 
    prepisat = input(f'Subor {vystupny_subor} uz existuje. Chcete ho prepisat? (ano/nie)')
    if prepisat != 'ano':
        exit()


with open(vstupny_subor, encoding='utf8') as fr:
    with open(vystupny_subor, 'w', encoding='utf8') as fw:
        for riadok in fr:
            riadok = riadok.rstrip('\r\n')  # Odstránime iba znaky nového riadku, nie medzery
            if riadok.strip().endswith(':'): # metoda hlada iba na konci
                # Načítáme hodnotu od uživatela
                print(riadok, end='')
                hodnota = input()
                fw.write(f'{riadok}{hodnota}\n')
            else:
                # Iba skopírujeme riadok do výstupného suboru
                fw.write(f'{riadok}\n')
        # Bonus 2
        datum = datetime.datetime.now().date()
        fw.write(datum.strftime('Datum: %d. %m. %Y'))
