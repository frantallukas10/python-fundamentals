# Tajná správa

# Napíšte definíciu funkcie desifruj, ktorá prijme zakódovanú vetu (všetko bude malými písmenami bez diakritiky a interpunkcie). Vašou úlohou je prečítať jednotlivé slová pospiatky a vrátiť celú dekódované správu.

def desifruj(tajna_sprava: str) -> str:
  """
  >>> desifruj('icap as im anaj')
  'paci sa mi jana'
  >>> desifruj('medjop recev tip')
  'pojdem vecer pit'
  """
  nova_sprava = []
  moja_sprava = tajna_sprava.split()
  for slovo in moja_sprava:
    nove_slovo = slovo[::-1] # prepise slovo naopak
    nova_sprava.append(nove_slovo)
  vysledok = ''
  for slovo  in nova_sprava:
    vysledok = vysledok + ' ' +  slovo
  return vysledok

print(desifruj('medjop recev tip'))