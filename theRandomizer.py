import random, os, sys, time

positive = ["YES", "YEAH!", "POSITIVE"]
negative = ["NO", "NOPE!", "NEGATIVE"]

spaces = [" ", "  ", "   ", "    "]

magicEightBall = [
    "IT IS CERTAIN",
    "IT IS DECIDEDLY SO",
    "WITHOUT A DOUBT",
    "YES, DEFINITELY",
    "YOU MAY RELY ON IT",
    "AS I SEE IT, YES",
    "MOST LIKELY",
    "OUTLOOK GOOD",
    "YES",
    "SIGNS POINT TO YES",
    "DON'T COUNT ON IT",
    "MY REPLY IS NO",
    "MY SOURCES SAY NO",
    "OUTLOOK NOT SO GOOD",
    "VERY DOUBTFUL",
    "ASK AGAIN LATER",
    "BETTER NOT TELL YOU NOW",
    "CANNOT PREDICT NOW",
    "CONCENTRATE AND ASK AGAIN"
]

helpText = """
COMMANDS:
<ITEM IN THE JAR>    - ADD ITEMS TO THE JAR
CLEAR | CLS          - CLEARS THE SCREEN
HELP | H             - PRINTS THIS
EXIT | QUIT          - KILLS THE PROGRAM
    [-Y | --YES]         - GIVES PERMISSION TO DELETE THE JAR
DONE                 - PICKS ITEM(S) FROM THE JAR
    [-T | --TIME TIME]   - ADDS DELAY (IN SECONDS) BETWEEN REMOVALS
    [-C | --COUNT COUNT] - SPECIFIES HOW MANY ITEMS TO PICK 
"""

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def confirmation(userInput, purpose, message="ARE YOU SURE? (Y | N) "):
    while True:
        choice = input(message).strip().upper()
        if choice in ["Y", "YES"]:
            if purpose == "KILL":
                sys.exit("GOODBYE!")
            elif purpose == "DUPLICATE":
                jar.append(userInput)
            break
        elif choice in ["N", "NO"]:
            break
        else:
            print("?!")

def pickSome(jar, howMany=1, delay=0):
    selected = []
    while len(selected) < howMany and jar:
        jar.remove(unfaithful := random.choice(jar))
        selected.append(unfaithful)
        if delay > 0:
            print(f"REMOVED: {unfaithful}")
            time.sleep(delay)
    if selected:
        print(f"FINAL CHOICE{'S' if len(selected) > 1 else ''}: {', '.join(map(str, selected))}")
    else:
        print("JAR IS VOID!")
    jar.clear()

def main():
    global jar
    jar = []
    clear()
    while True:
        userInput = input(f"~\\theRandomizer\choice{len(jar)+1}> ").strip()
        if not userInput:
            continue
        command = userInput.split()[0].upper()
        if command in ["CLEAR", "CLS"]:
            clear()
        elif command in ["HELP", "H"]:
            print(helpText)
        elif command in ["EXIT", "QUIT"]:
            if "-Y" in userInput.upper() or "--YES" in userInput.upper() or not jar:
                sys.exit("GOODBYE!")
            confirmation(None, "KILL", "THE JAR IS NOT VOID... QUIT ANYWAYS? (Y | N) ")
        elif command in ["YES", "NO"]:
            time.sleep(random.uniform(0.5, 3))
            print(random.choice(positive if command == "YES" else negative))
        elif command in ["MAGIC8BALL", "M8B"]:
            if len(userInput.split()) > 1:
                for _ in range(1, random.randint(15, 18)):
                    sys.stdout.write(f"\r{random.choice(spaces)}SHAKING   ")
                    sys.stdout.flush()
                    time.sleep(random.uniform(0.1, 0.2))
                sys.stdout.write("\r" + " " * 20 + "\r")
                sys.stdout.flush()
                print(random.choice(magicEightBall))
            else:
                print("I CANNOT PREDICT UNLESS I KNOW WHAT THE QUESTION IS")
        elif command == "DONE":
            args = userInput.split()[1:]
            timeDelay = 0
            count = 1
            i = 0
            while i < len(args):
                if args[i].upper() in ["-T", "--TIME"] and i + 1 < len(args).upper():
                    try:
                        timeDelay = max(0, float(args[i + 1]))
                        i += 2
                    except ValueError:
                        print("ERROR: TIME MUST BE A POSITIVE NUMBER!")
                        break
                elif args[i] in ["-C", "--COUNT"] and i + 1 < len(args):
                    try:
                        count = max(1, int(args[i + 1]))
                        i += 2
                    except ValueError:
                        print("ERROR: COUNT MUST BE A POSITIVE INTEGER!")
                        break
                else:
                    print(f"ERROR: UNKNOWN OPTION '{args[i].upper()}'")
                    break
            else:
                pickSome(jar, howMany=count, delay=timeDelay)
        else:
            if userInput in jar:
                confirmation(userInput, "DUPLICATE", f"'{userInput}' IS ALREADY IN THE JAR! ADD 'EM ANYWAYS? (Y | N) ")
            elif userInput:
                jar.append(userInput)

if __name__ == "__main__":
    main()
