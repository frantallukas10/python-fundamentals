# Nahraď znaky

# Na vstupe získate postupnosť znakov a jeden znak. V postupnosti nahraďte prvý výskyt tohto znaku za znak s obrátenou veľkosťou (napr. V za V alebo Z za z). Pomoc: funkcia replace s parametrom count a funkcie swapcase.

# Vyskúšajte tiež:
# aAaA A
# aaaa b

# Sample Input:
# AbCDabcd b

# Sample Output:
# ABCDabcd

vstup = input()
posledny_znak = vstup[-1] 
vystup = vstup[::-1].replace(posledny_znak, '', 1).strip()[::-1] # Najprv prevratim (vstup[::-1]), potom nahradím posledny znak za medzeru, biele znaky odstránim pomocou metody strip() a opat prevratim retazec

vystup = vystup.replace(posledny_znak, posledny_znak.swapcase(), 1)
print(vystup) 