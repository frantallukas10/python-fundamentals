# Napíšte definíciu funkcie funkcia4, ktorá zoberie ako parameter reťazec obsahujúci mena a priezvisko osôb oddelené čiarkami (pred a za čiarkou môže byť ľubovoľný počet medzier, medzi menami a priezviskom je jedna alebo viac medzier, každá osoba má iba jedno meno a jedno priezvisko) .Funkciu preformátuje mená osôb do formátu "Priezvisko, Meno", jednotlivé osoby oddelí bodkočiarkou a medzerou (pozri doctest). Návratovou hodnotou je takto prepracovaný reťazec.

from typing import Dict, List, Tuple
from pprint import pprint

def funkcia4(osoby: str) -> str:
      """Preformátuj mena.
      >>> funkcia4('Cyril   Novák ,    Alica Černá,Bob  Marley')
      'Novák, Cyril; Černá, Alica; Marley, Bob'
      """
      osoby = osoby.split(',')
      zoznam_preformatovanych = []
      for osoba in osoby:
            meno, priezvysko = osoba.split()  # split() bez argumentu automaticky združuje biele znaky, tj. nie je treba ich odstraňovat napríklad pomocou strip()
            zoznam_preformatovanych.append(f'{priezvysko}, {meno}')
      vysledok = '; '.join(zoznam_preformatovanych)
      return vysledok

print(funkcia4('Cyril   Novák ,    Alica Černá,Bob  Marley'))

