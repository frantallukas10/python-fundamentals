# Napíšte program, ktorý zo súboru cities.csv načíta súradnice miest. Program nájde najsevernejšej a najjužnejšie mesto a vypíše ich názvy a vzdialenosť (vzdušná čiarou).
# Pre zjednodušenie predpokladajme, že mestá sú umiestnené v rovine (Zeme je plochá). Súradnice x zdpovedaju smere západ-východ a súradnice y smere juh-sever. Vzdialenosť medzi bodmi A a B v rovine možno spočítať ako d AB = √ (xA-xB) 2+ (y A-y B) 2

import math
import csv

def main() -> None:
    with open('cities.csv', encoding='utf8') as csv_subor:
        reader = csv.reader(csv_subor, delimiter = " ", quotechar = "\"")
        maxY = -math.inf # nekonecno
        maxYCity = []
        minY = math.inf
        minYCity = []
        for line in reader:
            if len(line) != 3: # osetrenie
                continue
            if not line[1].isdigit() or not line[2].isdigit():
                continue
            if maxY < int(line[2]):
                maxY = int(line[2])
                maxYCity = line
            if minY > int(line[2]):
                minY = int(line[2])
                minYCity = line
    vzdialenost = str(math.sqrt(pow(int(maxYCity[1])-int(minYCity[1]), 2) + pow(int(maxYCity[2])-int(minYCity[2]), 2)))
    # sqrt () - odmocnina, pow () - mocnina
    
    print("najsevernejsie mesto je:", maxYCity[0])
    print("najjuznejsie mesto je:", minYCity[0])
    print("ich vzdialenost je:", vzdialenost)

main()
