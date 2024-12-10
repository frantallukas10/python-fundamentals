# Vyber data zo suboru .txt a uprav ich tak aby si spocital priemer jednotlivych pismen
numbers = {}

with open("ukazka1.txt") as txtfile: # txtfile je lubovolna premenna s ktorou budem pracovat
    for line in txtfile: # aby som precitala vsetky riadky
        key = line[0] # prvy znak v riadku
        number = float(line[1:].strip()) # alebo line[2:-1]
        if key not in numbers:
            numbers[key] = []
        numbers[key].append(number)

print(numbers) # {'A': [10.2, 10.1, 9.9, 10.3], 'B': [3.8, 4.2, 4.1], 'C': [6.0, 5.9, 6.3], 'D': [5000.1, 5000.0]}

for key, value in numbers.items(): # items, aby vracalo nie len kluc ale aj hodnotu
    print(key, sum(value)/len(value))
# A 10.125
# B 4.033333333333333
# C 6.066666666666666
# D 5000.05
