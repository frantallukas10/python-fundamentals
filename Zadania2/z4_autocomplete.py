# Napíšte program, ktorý načíta zo súboru phrases.txt zoznam často hľadaných fráz a ich frekvencia vyhľadávania (každý riadok je vo formáte frekvencia: frázy).
# Potom bude program načítať zo štandardného vstupu začiatky fráz (jeden začiatok na každom riadku) a ku každému začiatku vypíše všetky vyhovujúce frázy zoradené podľa klesajúcej frekvencie. Program skončí, keď bude zo vstupu zadaný prázdny riadok.

# how to # vstup
# - how to learn python
# - how to make plutonium
# blablabla # vstup
# what # vstup
# - what is the meaning of life
# - what is justin bieber's favourite colour
# wh # vstup
# - what is the meaning of life
# - who is justin bieber
# - what is justin bieber's favourite colour

def main() -> None:
    phrases = {}
    with open('phrases.txt', mode='r', encoding='utf8') as f:
        text = f.read()
        text = text.split("\n")
        for line in text:
            thing = line.split(":")
            if len(thing) != 2:
                continue

            phrases[thing[1]] = float(thing[0])
        print(phrases)
        # {'can i type google into google': 6.8, 'diameter of the earth': 45.2, 'five strange vegetables that will help me lose weight': 22.1, 'how many cm is one foot': 25.0, 'how to learn python': 100.0, 'how to make plutonium': 27.8, 'is python gluten free': 18.0, "what is justin bieber's favourite colour": 12.5, 'what is the meaning of life': 80.0, 'who is justin bieber': 30.5}

        sorted_phrases = [k for k, _ in sorted(phrases.items(), key=lambda item: item[1], reverse=True)]
        print(sorted_phrases)
        # ['how to learn python', 'what is the meaning of life', 'diameter of the earth', 'who is justin bieber', 'how to make plutonium', 'how many cm is one foot', 'five strange vegetables that will help me lose weight', 'is python gluten free', "what is justin bieber's favourite colour", 'can i type google into google']

    userInput = input()
    while userInput != '':
        for phrase in sorted_phrases:
            if userInput == phrase[0:len(userInput)]:
                print("- " + phrase)
        userInput = input()

main()
