# Začína, končí alebo obsahuje?
# Na vstupe získate dva reťazca. Otestujte či prvý reťazec začína, končí alebo iba obsahuje druhý reťazec.

# Možné výstupy:

# "{}" začína a končí "{}"
# "{}" začína "{}"
# "{}" končí "{}"
# "{}" obsahuje "{}"
# "{}" neobsahuje "{}"
# Miesto {} doplňte prvý a druhý reťazec.

# Sample Input:
# abcabc abc

# Sample Output:
# "abcabc" začína a končí "abc"

kopka_slamy, ihla = input().split()
realita = ihla in kopka_slamy

if realita == True:
    if kopka_slamy.startswith(ihla) and kopka_slamy.endswith(ihla) == True:
        print(f'"{kopka_slamy}" začína a končí "{ihla}"')
    elif kopka_slamy.startswith(ihla) == True:
        print(f'"{kopka_slamy}" začína "{ihla}"')
    elif kopka_slamy.endswith(ihla) == True:
        print(f'"{kopka_slamy}" končí "{ihla}"')
    elif realita:
        print(f'"{kopka_slamy}" obsahuje "{ihla}"')
else:
    print(f'"{kopka_slamy}" neobsahuje "{ihla}"')

