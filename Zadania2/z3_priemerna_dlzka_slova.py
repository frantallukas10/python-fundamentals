# Napíšte definíciu funkcie priemerna_dlzka_slova, ktorá zoberie ako parameter reťazec obsahujúci text a vráti priemernú dĺžku slová v tomto texte.
# Text bude obsahovať len písmená, medzery, čiarky a bodky. Pokiaľ bude medzi dvoma slovami čiarka alebo bodka, vždy za ňou bude medzera. Tieto predpoklady nemusíte v kóde kontrolovať. Výsledok nie je nutné zaokrúhľovať, postará sa o to funkcia round v doctestu. Ak priemernú dĺžku slová z nejakého dôvodu nemožno spočítať, funkcia má vyhodiť výnimku typu ValueError.


import math

def priemerna_dlzka_slova(text: str) -> float:
    """
    >>> round(priemerna_dlzka_slova('prva ukážka'), ndigits=3)
    5.5
    >>> round(priemerna_dlzka_slova('Dobrý deň.'), ndigits=3)
    4.0
    >>> round(priemerna_dlzka_slova('Orol klínoocasý je druh vtáka, ktorý sa vyskytuje v Austrálii a Tasmánii, na juhu Novej Guiney a blízkych ostrovoch. Patrí medzi najväčšie druhy orlov vôbec a je to najväčší dravý vták Austrálie.'), ndigits=3)
    5.125
    >>> round(priemerna_dlzka_slova('Skutok ... utek'), ndigits=3)
    5.0
    >>> round(priemerna_dlzka_slova('...'), ndigits=3)
    Traceback (most recent call last):
    ValueError
    """
    sucet = 0
    vstupne_pole = text.split()
    pocet_slov = len(vstupne_pole)
    for slovo in vstupne_pole:
        if slovo[len(slovo) - 1] == '.' or slovo[len(slovo) - 1] == ',':
            slovo = slovo[0:len(slovo) - 1]

        if not slovo.isalnum():
            pocet_slov -= 1
            continue

        dlzka_slova = len(slovo)
        sucet = sucet + int(dlzka_slova)

    if pocet_slov == 0:
        raise ValueError
    priemerna_dlzka_slova = float(sucet) / float(pocet_slov)
    return priemerna_dlzka_slova

print(priemerna_dlzka_slova('Dobrý deň.'))