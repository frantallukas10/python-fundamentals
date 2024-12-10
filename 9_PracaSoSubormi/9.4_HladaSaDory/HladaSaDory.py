"""
Úloha:
Vytvorte program, ktorý prejde všetky súbory v adresári CSFD a vypíše
na výstup názvy všetkých súborov obsahujúcich v texte slovo Dory.

Vzorový výstup:  
Hleda_se_Dory.txt
Hleda_se_Nemo.txt

Bonus:
Modifikujte program tak, aby prehľadával celý adresárový strom.
Tj. aby našiel napríklad tiež súbor  CSFD/Pohadky/Animovane/Hleda_se_Nemo.txt.
"""

import glob
import os
from os import path

def subor_obsahuje(nazov_suboru: str, hladany_subor: str, encoding='utf8') -> bool: # type boolean
    """
    Zisti, či súbor názov_súboru vo svojom texte obsahuje hladany_text.
     Vráť False, ak súbor nemožno otvoriť alebo sa jedná o adresár.
    """
    try:
        with open(nazov_suboru, encoding=encoding) as f:
            text = f.read() # precitanie suboru
        return hladany_subor in text
    except (FileNotFoundError, PermissionError, IsADirectoryError):
        return False

hladane_slovo = 'Dory'

os.chdir('CSFD') # zmena pracovneho adresara pomocou os modulu
subory = glob.glob('**', recursive=True) # vypise vsetky subory v adresari vratane podurovni

# # ine riesenie
# os.chdir('CSFD')
# subory = os.listdir() # vracia obsah adresaru

for subor in subory:
    if subor_obsahuje(subor, hladane_slovo):
        print(subor)
