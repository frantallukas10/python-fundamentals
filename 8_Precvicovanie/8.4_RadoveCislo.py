# Radové číslovky

# Napíšte definíciu funkcie ordinal, ktorá ako argument prijme prirodzené číslo a vráti zodpovedajúcu radovú číslovku v angličtine (tj. 1st, 2nd, 3rd, 4th, 11th, 20th, 23rd, 151st, 2012th a pod.).

def ordinal(number: int) -> str:
    """
    >>> ordinal(5)
    '5th'
    >>> ordinal(151)
    '151st'
    """
    if number < 20:
        if number == 1:
            pripona = 'st'
        elif number == 2:
            pripona = 'nd'
        elif number == 3:
            pripona = 'rd'
        else:
            pripona = 'th'  
    else:   #determining pripona pre > 20
        desiatky = str(number)
        desiatky = desiatky[-2]
        jednotky = str(number)
        jednotky = jednotky[-1]
        if desiatky == "1":
            pripona = "th"
        else:
            if jednotky == "1": 
                pripona = 'st'
            elif jednotky == "2":
                pripona = 'nd'
            elif jednotky == "3":
                pripona = 'rd'
            else:
                pripona = 'th'
    return str(number)+pripona

print(ordinal(22))