# Riešime kvadratickú rovnicu pomocou funkcie

# Napíšte definíciu funkcie korene, ktorá prijíma tri číselné parametre a, b, c. Výstupom funkcie budú korene kvadratickej rovnice v n-ticu. Počítajte s tým, že zadaná kvadratická rovnica môže mať dva, jeden alebo žiadny koreň.

# Sample Input 1:
# korene(1.0, -5.0, 6.0)

# Sample Output 1:
# (3.0, 2.0)

# Sample Input 2:
# korene(1.0, -2.0, 1.0)

# Sample Output 2:
# (1.0,)

from typing import Tuple

def korene(a: float, b: float, c: float) -> Tuple[float, float]:
    D = b**2 - 4*a*c
    if D > 0:
      x2 = (-b + D**0.5) / (2*a)
      x1 = (-b - D**0.5) / (2*a)
      return (x1, x2)
    elif D == 0:
      x = (-b) / 2*a
      return (x,)
    else:
      return ()

print(korene(1.0, -2.0, 1.0)) 




