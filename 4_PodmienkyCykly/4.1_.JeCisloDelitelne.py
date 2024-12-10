# Je číslo deliteľné?

# Na vstupe získame celé číslo od 0 do 100.
# 1. otestujte, či sme dostali správne číslo (medzi 0 a 100)
# 2. otestujte, či je číslo deliteľné piatimi, tromi alebo oboma číslami zároveň

# Na výstup vypíšte:
# - zlé číslo
# - číslo je deliteľné 3 a 5
# - číslo je deliteľné 3
# - číslo je deliteľné 5
# - číslo nie je deliteľné 3 ani 5

# Sample Input:
# 4

# Sample Output:
# číslo nie je deliteľné 3 ani 5

vstup = int(input())

if vstup >= 0 and vstup <= 100:
    if vstup % 3 == 0 and vstup % 5 == 0:
        print("číslo je deliteľné 3 a 5")
    elif vstup % 3 == 0:
        print("číslo je deliteľné 3")
    elif vstup % 5 == 0:
        print("číslo je deliteľné 5")
    elif vstup % 3 != 0 and vstup % 5 != 0:
        print("číslo nie je deliteľné 3 ani 5")
else: 
    print("zlé číslo")