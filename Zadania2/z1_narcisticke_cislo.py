# Narcisticke číslo je číslo, ktoré je rovné súčtu svojich cifier umocnená na počet cifier.
# Napr. číslo 8208 je narcisticke, pretože 8 ^ 4 + 2 ^ 4 + 0 ^ 4 + 8 ^ 4 = 8208.
# Napíšte definíciu funkcie je_narcisticke, ktorá zoberie prirodzené číslo n a vráti True, práve vtedy, keď n je narcisticke číslo.

def je_narcisticke(n: int) -> bool:
    """
    >>> je_narcisticke(5)
    True
    >>> je_narcisticke(10)
    False
    >>> je_narcisticke(42)
    False
    >>> je_narcisticke(153)
    True
    >>> je_narcisticke(8028)
    True
    """
    sucet = 0
    pocet_cifier = len(str(n))
    n = str(n)
    for cifra in n:
      medzi_sucet = int(cifra) ** int(pocet_cifier)
      sucet = sucet + int(medzi_sucet)
    return int(sucet) == int(n)
      
print(je_narcisticke(153))