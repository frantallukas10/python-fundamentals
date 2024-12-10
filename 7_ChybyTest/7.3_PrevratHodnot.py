# Prevrátená hodnota

# Zadaný vstup sa pokúste previesť na číslo N, a vypočítajte pre neho prevrátenú hodnotu 1 / N. Ak sa to nepodarí, vypíšte None.

# Sample Input 1:
# 10

# Sample Output 1:
# 0.1

# Sample Input 2:
# 0

# Sample Output 2:
# None

try:
    N = int(input())
    n = 1 / N
    print(n)
except (ZeroDivisionError, ValueError):
    print(None)