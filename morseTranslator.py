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
    '.-.-.-', '--..--', '..--..', '.----.', '-.-.--', '-..-.', '-....-', '.-..-.', '---...', '-.-.-.', '-...-', '.-.-.', '--..--.', '..--.-', '.--.-.'
]

nonMORSE = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    '.', ',', '?', "'", '!', '/', '-', '"', ':', ';', '=', '_', '@'
]

morseDict = dict(zip(nonMORSE, MORSE))
reverseMD = dict(zip(MORSE, nonMORSE))

def checkInput(uI):
    allowedChars = set(nonMORSE + [' '])
    return all(char.upper() in allowedChars for char in uI)

def translate(userInput, isRegular):
    if isRegular:
        words = userInput.upper().split()
        transWords = []
        for word in words:
            transChar = [morseDict.get(char, '') for char in word]
            transWords.append(' '.join(transChar))
        morseCode = ' / '.join(transWords)
        print(f"MORSE: {morseCode}")
    else:
        transWords = []
        for morseWord in userInput.split(' / '):
            transChar = [reverseMD.get(code, '') for code in morseWord.split()]
            transWords.append(''.join(transChar))
        plainText = ' '.join(transWords)
        print(f"TEXT: {plainText}")

def main():
    clear()
    while True:
        uInput = input("~\\morseTranslator$ ").strip()
        cmd = uInput.split()[0].upper()

        if cmd in {"CLS", "CLEAR"}:
            clear()
        elif cmd in {"EXIT", "QUIT"}:
            sys.exit("GOODBYE!")
        elif cmd in {"HELP"}:
            print(helpText)
        else:
            if any(char in uInput for char in '.-/'):
                translate(uInput, isRegular=False)
            elif checkInput(uInput):
                translate(uInput, isRegular=True)
            else:
                print("INVALID INPUT!")
                
if __name__ == "__main__":
    main()