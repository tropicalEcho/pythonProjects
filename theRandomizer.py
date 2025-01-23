import random, os, sys, time

help_text = """
COMMANDS:
<ITEM>               Add item to the jar
CLEAR | CLS          Clear the screen
HELP | H             Show this help message
LIST | LS            Show contents of the jar
EXIT | QUIT          Exit the program
    [-Y | --YES]     Skip confirmation when exiting
DONE                 Pick item(s) from the jar
    [-T | --TIME]    Delay between removals (seconds)
    [-C | --COUNT]   Number of items to pick
YESNO | YN           Get a random yes/no answer
"""

jar = []

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def confirmation(message):
    while True:
        response = input(message).strip().upper()
        if response in {'Y', 'YES'}:
            return True
        if response in {'N', 'NO'}:
            return False
        print("INVALID INPUT! Y/N")

def showJar():
    if not jar:
        print("JAR IS EMPTY!")
        return
    
    counts = {}
    for item in jar:
        counts[item] = counts.get(item, 0) + 1
    
    print("\nJAR CONTENTS:")
    for idx, (item, count) in enumerate(counts.items(), 1):
        print(f"{idx:>3}. {item} ({count}x)")

def pickItems(howMany=1, delay=0):
    selected = []
    originalJar = jar.copy()
    
    try:
        while len(selected) < howMany and jar:
            choice = random.choice(jar)
            jar.remove(choice)
            selected.append(choice)
            if delay > 0:
                print(f"REMOVED: {choice.upper()}")
                time.sleep(delay)
        
        if selected:
            final = "FINAL SELECTION" + ("S:" if len(selected) > 1 else ": ")
            print(f"{final} {', '.join(selected)}")
        else:
            print("JAR IS EMPTY")
    except KeyboardInterrupt:
        print("\nSELECTION INTERRUPTED!")
        jar.clear()
        jar.extend(originalJar)
        if selected:
            print(f"PARTIAL SELECTION: {', '.join(selected)}")

def handleDone(arguments):
    count = 1
    delay = 0
    i = 0
    
    while i < len(arguments):
        arg = arguments[i].upper()
        try:
            if arg in {'-T', '--TIME'}:
                delay = max(0, float(arguments[i+1]))
                i += 2
            elif arg in {'-C', '--COUNT'}:
                count = max(1, int(arguments[i+1]))
                i += 2
            else:
                print(f"UNKNOWN OPTION: {arguments[i]}")
                return
        except (IndexError, ValueError):
            print("INVALID VALUE FOR OPTION:", arg)
            return
    
    pickItems(count, delay)

def handleExit(arguments):
    if '-Y' in arguments or '--YES' in arguments or not jar:
        sys.exit("GOODBYE!")
    if confirmation("JAR NOT EMPTY! EXIT ANYWAYS? (Y/N) "):
        sys.exit("GOODBYE!")

def randomAnswer():
    time.sleep(random.uniform(0.5, 1.5))
    print(random.choice(["YES", "NO"]))

def main():
    clear()
    print("WELCOME TO theRandomizer!\n")
    
    while True:
        try:
            prompt = input(f"~\\theRandomizer\\[{len(jar)+1}]> ").strip()
            
            if not prompt:
                continue
            
            promtParts = prompt.split()
            cmd = promtParts[0].upper()
            arguments = promtParts[1:]
            
            if cmd in {'CLEAR', 'CLS'}:
                clear()
            elif cmd in {'HELP', 'H'}:
                print(help_text)
            elif cmd in {'EXIT', 'QUIT'}:
                sys.exit("GOODBYE!")
            elif cmd == 'DONE':
                handleDone(arguments)
            elif cmd in {'YESNO', 'YN'}:
                randomAnswer()
            elif cmd in {'LIST', 'LS'}:
                showJar()
            else:
                item = ' '.join(promtParts)
                jar.append(item)
        
        except KeyboardInterrupt:
            print("\nUSE 'EXIT' OR 'QUIT' TO KILL THE PROGRAM")
        except EOFError:
            sys.exit("\nERROR: GOTTA GO!")

if __name__ == "__main__":
    main()
