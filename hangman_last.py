import random,time,sys

european_capitals = ["TIRANA", "ANDORRA", "YEREVAN", "VIENNA", "BAKU", "MINSK", "BRUSSELS",
"SARAJEVO", "SOFIA", "ZAGREB", "NICOSIA", "PRAGUE", "COPENHAGEN", "TALLINN", "HELSINKI", "PARIS",
"TBILISI","BERLIN", "ATHENS", "BUDAPEST", "REYKJAVIK", "DUBLIN", "ROME", "ASTANA", "PRISTINA",
"RIGA", "VADUZ", "VILNIUS", "LUXEMBOURG", "SKOPJE", "VALLETTA", "CHISINAU", "MONACO", "PODGORICA",
"AMSTERDAM", "OSLO", "WARSAW", "LISBON", "BUCHAREST", "MOSCOW", "SANMARINO", "BELGRADE",
"BRATISLAVA", "LJUBLJANA", "MADRID", "STOCKHOLM", "BERN", "ANKARA", "KYIV", "LONDON", "VATICAN"]


life = 5
missedUserInputs = []
dashesList = []
gameover = ("""
   __ _   __ _   _ __ ___     ___    ___   __   __   ___   _ __
  / _` |  / _` | | '_ ` _ \   / _ \  / _ \  \ \ / /  / _ \ | '__|
 | (_| | | (_| | | | | | | | |  __/ | (_) |  \ V /  |  __/ | |
  \__, |  \__,_| |_| |_| |_|  \___|  \___/    \_/    \___| |_|
  |___/
""")

win = ("""
 __   __   ___    _   _    __        __  ___   _   _   _
 \ \ / /  / _ \  | | | |   \ \      / / |_ _| | \ | | | |
  \ V /  | | | | | | | |    \ \ /\ / /   | |  |  \| | | |
   | |   | |_| | | |_| |     \ V  V /    | |  | |\  | |_|
   |_|    \___/   \___/       \_/\_/    |___| |_| \_| (_)

""")

def randomCity():
    """Random city from european_capitals list"""
    randomCity = random.choice(european_capitals)
    convertLetterToDash(randomCity)
    return randomCity


def convertLetterToDash(randomCity):
    """Convert letters into dashes"""
    for i in range(0,len(randomCity)):
        dashesList.append(" _ ")
        print(dashesList[i],end = " ")


def wordOrLetter(varRandomCity):
    """Check input from user and do right option"""

    while True:
        userInputNumber = input("\nEnter 1-word or 2-letter or any other"
        +" key to exit: ")

        global life
        if userInputNumber == "1":
            guess_word = input("Guess word: ")
            guess_word = guess_word.upper()
            if life > 1:
                    if guess_word == varRandomCity:
                        print(win)
                        print("*** Life: "+str(life)+" ***")
                        break
                        sys.exit(0)
                    else:
                        life -= 1
                        print("It's not correct word, you loose 1 life!")
                        print("*** Life: "+str(life)+" ***")

            else:
                print(gameover+" Correct answer "+varRandomCity)
                break
        elif userInputNumber == "2":
            checkLetter(varRandomCity)
        else:
            print("Ending program...")
            time.sleep(2)
            sys.exit(0)


def checkLetter(varRandomCity):
    """Check letters in varRandomCity and replace with dashesList """
    global life
    userLetterInput = input("Guess a letter: ")
    userLetterInput = userLetterInput.upper()

    for index in range(len(varRandomCity)):
        if userLetterInput == varRandomCity[index]:
            dashesList[index] = userLetterInput


    for i in range(0,len(dashesList)):
        print(dashesList[i],end=" ")

    if life > 1:
        if userLetterInput in varRandomCity:
            print("Hit!")
            print("*** Life: "+str(life)+" ***")
            length = len(dashesList)
            for i in range(0,len(dashesList)):
                if dashesList[i] == " _ ":
                    length -= 1
            if length == len(dashesList):
                print(win)
                sys.exit(0)

        elif userLetterInput not in varRandomCity:
            print("It's not correct letter, you loose 1 life!")
            missedUserInputs.append(userLetterInput)
            print("Fail user letter =>",missedUserInputs,end=" ")
            life -= 1
            print("\n*** Life: "+str(life)+" ***")
    else:
        print(gameover+" Correct answer "+varRandomCity)
        sys.exit(0)


def main():
    print("Welcome to Hangman Game!")
    print("""
                            | |
            __      __  ___ | |  ___   ___   _ __ ___    ___
            \\ \\ /\ / / / _ \\| | / __| / _ \\ | '_ ` _ \\  / _ \\
             \ V  V / |  __/| || (__ | (_) || | | | | ||  __/
              \_/\_/   \___||_| \___| \___/ |_| |_| |_| \___|
        """)
    print("""
            | |
            | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
            | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
            | | | | (_| | | | | (_| | | | | | | (_| | | | |
            |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                __/ |
                               |___/
    """)
    print("Remember, you are looking for an european capital!\n")
    print("*** Life: "+str(life)+" ***")
    varRandomCity = randomCity()
    print(varRandomCity)
    wordOrLetter(varRandomCity)


main()
