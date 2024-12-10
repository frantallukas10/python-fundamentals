# Nahraď slová

# V zadanom texte nájdite všetky výskyty slova "je" a nahraďte ich za slovo "bude". Nezabudnite opravený text vypísať.

# Sample Input:
# Lukáš je doktor.

# Sample Output:
# Lukáš bude doktor.

string = input()
nahrada = string.replace('je', 'bude')
print(nahrada)