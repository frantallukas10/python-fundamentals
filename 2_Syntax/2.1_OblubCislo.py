# obľúbené čísla

# Alice, Bob a Cyril si chcú vybrať spoločné obľúbené číslo.

# Alicu sa páči dvojciferné čísla, ktoré obsahujú štvorku.
# Bobovi sa páči čísla deliteľné tromi.
# Cyrilovi sa páči všetky čísla okrem násobkov siedmich.
# Zistite, či sa zadané prirodzené číslo n bude páčiť všetkým trom.

# Sample Input 1:
# 45

# Sample Output 1:
# True

# Sample Input 2:
# 42

# Sample Output 2:
# False

# Sample Input 3:
# 12

# Sample Output 3:
# False

n = int(input())

libi_se_vsem = (n > 9 and n < 100 and '4' in str(n) and n % 3 == 0 and n % 7 != 0)

print(libi_se_vsem)