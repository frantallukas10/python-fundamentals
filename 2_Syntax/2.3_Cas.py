# CAS

# Čas t (v sekundách) vyjadřrite ako počet celých hodín h, minút m a sekund s.

# Sample Input 1:
# 90

# Sample Output 1:
# 0:01:30

# Sample Input 2:
# 3600

# Sample Output 2:
# 1:00:00


t = int(input())

h = t//3600
t = t%3600
m = t//60
s = t%60

print(f'{h}:{m:>02}:{s:02}')