# Stratené v preklade

# Napíšte definíciu funkcie prepoj_slovniky, ktorá berie dva argumenty: slovník z češtiny do angličtiny a slovník z angličtiny do slovenčiny. Funkcia by mala vrátiť slovník z češtiny do slovenčiny.

def prepoj_slovniky(cz_en: dict, en_sk: dict) -> dict:
    """
    >>> prepoj_slovniky({'kachna': 'duck', 'kočka': 'cat', 'pes': 'dog'}, {'cat': 'mačka', 'dog': 'pes', 'duck': 'kačka'})
    {'kachna': 'kačka', 'kočka': 'mačka', 'pes': 'pes'}
    """
    result_dict = {}
    for cesky, anglicky in cz_en.items(): #   .items() vracia pole dvojic (kluc, hodnota)
        result_dict[cesky] = en_sk[anglicky] #  do resultoveho slovniku pridam novy entry pod cesky nazov taky aky je v en_sk pod anglickym

    return result_dict

print(prepoj_slovniky({'kachna': 'duck', 'kočka': 'cat', 'pes': 'dog'}, {'cat': 'mačka', 'dog': 'pes', 'duck': 'kačka'}))
