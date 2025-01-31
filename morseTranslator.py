import os, sys

def clear():
    os.system("cls" if os.name == "nt" else "clear")

helpText = """
HELP           PRINTS THIS
CLEAR | CLS    CLEARS SCREEN
EXIT | QUIT    KILLS THE PROGRAM
<TEXT>         TRANSLATES REGULAR TEXT TO MORSE CODE
<MORSE>        TRANSLATES MORSE CODE TO REGULAR TEXT
"""

MORSE = [
    '.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..',
    '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.',
    '.-.-.-', '--..--', '..--..', '.----.', '-.-.--', '-..-.', '-....-', '.-..-.', '---...', '-.-.-.', '-...-', '.-.-.', '/--.-'
]

nonMORSE = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    '.', ',', '?', "'", '!', '-', '/', '"', ':', ';', '=', '@'
]

morseDict    = dict(zip(nonMORSE, MORSE))
upsideDownMD = dict(zip(MORSE, nonMORSE))

def checkInput(uI):
    for char in uI: 
        if char.upper() not in nonMORSE and char != ' ':
            return False
    return True

def translate(userInput, isRegular):
    if isRegular:
        userInput = userInput.upper()
        morseCode = ' '.join([morseDict.get(char, '') for char in userInput if char != ' '])
        print(f"MORSE: {morseCode}")
    else:
        morseChars = userInput.split(' ')
        translatedText = ''.join([reverseMorseDict.get(code, '') for code in morseChars if code != ''])
        print(f"TEXT: {translatedText}")

def main():
    clear()
    while True:
        uINPUT = input("~\\morseTranslator$ ").strip()
        cmd = uINPUT.split()[0].upper()

        if cmd in {"CLS", "CLEAR"}:
            clear()
        elif cmd in {"EXIT", "QUIT"}:
            sys.exit("GOODBYE!")
        elif cmd in {"HELP"}:
            print(helpText)
        else:
            if checkInput(uINPUT):
                if any(char in uINPUT for char in '.-'):
                    translate(uINPUT, isRegular=False)
                else: 
                    translate(uINPUT, isRegular=True)
            else:
                print("INVALID INPUT!")
                
if __name__ == "__main__":
    main()
