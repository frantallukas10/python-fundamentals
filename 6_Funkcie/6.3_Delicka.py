# Delicka

# Napíšte funkciu Delicka, ktorá bude prijímať parameter text a voliteľný parameter separator (defaultný separátor = ';'). Rozdeľuje text podľa parametra separator, prevedie prvé dva prvky na reálne čísla a vráti ich podiel.

# Sample Input 1:
# delicka('1;2;haha')

# Sample Output 1:
# 0.5

# Sample Input 2:
# delicka('3 2 ... ... ...', separator=' ')

# Sample Output 2:
# 1.5

def delicka(text: str, separator: str = ';') -> float:
    prvy, druhy, *_ = text.split(separator)
    return float(prvy) / float(druhy)

print(delicka('1;2;haha'))

# # Alternatívne riešenie:
# def delicka(text: str, separator: str = ';') -> float:
#     prvky = text.split(separator)
#     return float(prvky[0]) / float(prvky[1])

# print(input())


