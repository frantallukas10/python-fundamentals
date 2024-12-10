# Fibonacciho postupnosti

# Napíšte funkciu, ktorá získa ako parameter počet prvkov Fibonacciho postupnosti a tie vráti vo forme zoznamu.

# Sample Input:
# fibonacci(6)

# Sample Output:
# [1, 1, 2, 3, 5, 8]

from typing import List
zoznam = []
def fibonacci(n: int) -> List[int]:
    vysledok = []
    a = 1
    b = 1
    for i in range(n):
        vysledok.append(b)
        scitanec = b + a
        b = a
        a = scitanec
    return vysledok

print(fibonacci(6))

# # Alternatívne riešenie:
# from typing import List

# def fibonacci(n: int) -> List[int]:
#     if n == 0:
#         return []
#     elif n == 1:
#         return [1]
#     else:
#         vysledok = [1, 1]
#         while len(vysledok) < n:
#             nove_cislo = vysledok[-2] + vysledok[-1]
#             vysledok.append(nove_cislo)
#         return vysledok

# print(fibonacci(6))  


# # Alternatívne riešenie:
# from typing import List

# def fibonacci(n: int) -> List[int]:
#     if n == 0:
#         return []
#     elif n == 1:
#         return [1]
#     else:
#         vysledok = [1, 1]
#         for i in range(n - 2):
#             vysledok.append(sum(vysledok[-2:]))
#         return vysledok

# print(fibonacci(6))  

