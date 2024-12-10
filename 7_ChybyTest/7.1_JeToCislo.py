# Je to číslo?

# Na vstupe získate reťazec, zistite či je to desatinné číslo. Ak áno, vypíšte True; ak nie, vypíšte False.

# Sample Input 1:
# -8.3

# Sample Output 1:
# True

# Sample Input 2:
# abc

# Sample Output 2:
# False

try:
    float(str(input()))
    print(True)
except ValueError:
    print(False)