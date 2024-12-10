# Hladanie cisel

# Na vstupe získate zoznam čísel oddelených medzerou. Spočítajte a vypíšte minimum, maximum, priemer a medián. Vypíšte posledné číslo.

# Vyskoušajte i tento vstup:
# 3 9 4 8 2 1

# Sample Input:
# 15 13 7 10 11

# Sample Output:
# Min: 7.00 Max: 15.00 Avg: 11.20 Med: 11.00
# Last number: 11

moj_zoznam = input().split()
dlzka = len(moj_zoznam) # pocet cisel v zozname
for prvok in range(0, dlzka):
    moj_zoznam[prvok] = int(moj_zoznam[prvok])
# moj_zoznam = [int(x) for x in moj_zoznam]    
sortovany_zoznam = sorted(moj_zoznam, reverse=False) # [7, 10, 11, 13, 15]
maxi = max(moj_zoznam) # maximalne cislo
mini = min(moj_zoznam) # minimalne cislo
avg = (sum(moj_zoznam) / dlzka) # priemer
x = round(dlzka / 2) # zaokruhly
if dlzka % 2 != 0:
    med = sortovany_zoznam[x]
else:
    med = ((int(sortovany_zoznam[x - 1]) + int(sortovany_zoznam[x])) / 2)
    
posledne_cislo = moj_zoznam.pop() # posledne cislo

print('Min:', '{:.2f}'.format(mini), 'Max:', '{:.2f}'.format(maxi), 'Avg:', '{:.2f}'.format(avg), 'Med:','{:.2f}'.format(med))
print('Last number:', posledne_cislo)

#----------------------------------------------------
# import statistics

# vstup = input()
# retezce = vstup.split()
# cisla = [int(r) for r in retezce]
# minimum = min(cisla)
# maximum = max(cisla)
# prumer = statistics.mean(cisla)
# median = statistics.median(cisla)
# posledni = cisla[-1]
# print(f'Min: {minimum:.2f} Max: {maximum:.2f} Avg: {prumer:.2f} Med: {median:.2f}')
# print(f'Last number: {posledni}')