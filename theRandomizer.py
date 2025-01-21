import random
import os
import sys
import time
import json
from datetime import datetime, timedelta

jar = []
saveJar = False
history = []
historyFile = "randomizer_history.json"

try:
    with open(historyFile, 'r') as f:
        history = json.load(f)
except FileNotFoundError:
    history = []

# Save actions to history and persist to a file
def save2History(command, input_data, result):
    entry = {
        'when': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'what': command,
        'input': input_data,
        'result': result
    }
    history.append(entry)
    with open(historyFile, 'w') as f:
        json.dump(history, f, indent=2)

# Clear the terminal screen
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Generate a random number between start and end
def get_random_number(start, end):
    return random.randint(start, end)

# Roll a dice with a specified number of faces
def roll_dice(FACES=6):
    return random.randint(1, FACES)

# Generate a random time between start and end (HH:MM:SS format)
def get_random_time(start=None, end=None):
    if not start and not end:
        seconds = random.randint(0, 86399)
        return time.strftime('%H:%M:%S', time.gmtime(seconds))

    t1 = sum(int(x) * 60 ** i for i, x in enumerate(reversed(start.split(':'))))
    t2 = sum(int(x) * 60 ** i for i, x in enumerate(reversed(end.split(':'))))
    return time.strftime('%H:%M:%S', time.gmtime(random.randint(t1, t2)))

# Simulate a coin flip
def flip_coin():
    return random.choice(["HEADS", "TAILS"])

# Generate a random date between start and end (YYYY-MM-DD format)
def get_random_date(start, end):
    date1 = datetime.strptime(start, '%Y-%m-%d')
    date2 = datetime.strptime(end, '%Y-%m-%d')
    days_between = (date2 - date1).days
    return (date1 + timedelta(days=random.randint(0, days_between))).strftime('%Y-%m-%d')

# Shuffle a list of items
def scramble_list(items):
    shuffled = items.copy()
    random.shuffle(shuffled)
    return shuffled

# Generate a random color in RGB and HEX formats
def get_random_color():
    r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    return f"RGB({r},{g},{b}) | #{r:02x}{g:02x}{b:02x}"

# Pick a random playing card
def get_random_card():
    suits = ['\u2660', '\u2663', '\u2665', '\u2666']  # Unicode for card suits
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    return f"{random.choice(values)}{random.choice(suits)}"

# Pick a random chemical element
def get_element():
    elements = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne"]
    return random.choice(elements)

# Pick a random country
def get_random_country():
    countries = ["USA", "UK", "India", "Japan", "Canada"]
    return random.choice(countries)

# Pick items from the jar
# Optionally removes picked items if saveJar is off
def pick_from_jar(count=1, delay=0):
    global jar
    if not jar:
        return []

    picked = []
    for _ in range(min(count, len(jar))):
        item = random.choice(jar)
        jar.remove(item)
        picked.append(item)
        if delay > 0:
            print(f"PICKED: {item}")
            time.sleep(delay)

    if not saveJar:
        jar.clear()
    return picked

# Display help text for commands
helpText = """
COMMANDS:
NUM start end       - RANDOM NUMBER
DICE [FACES]        - ROLL DICE (DEFAULT: 6)
TIME [HH:MM:SS]     - RANDOM TIME
COIN                - FLIP A COIN
DATE start end      - RANDOM DATE
MIX <ITEMS>         - SCRAMBLE LIST
COLOR               - RANDOM COLOR
CARD                - RANDOM CARD
ELEM                - RANDOM ELEMENT
LAND                - RANDOM COUNTRY
ADD <ITEM>          - ADD TO JAR
PICK [N] [DELAY]    - PICK FROM JAR
KEEP                - TOGGLE KEEP ITEMS
HIST [N]            - SHOW HISTORY (DEFAULT: 5)
CLEAR               - CLEAR SCREEN
HELP                - SHOW HELP TEXT
EXIT                - QUIT
"""

# Main interactive loop
def main():
    global jar, saveJar
    clear()

    while True:
        try:
            cmd = input(f"~\\theRandomizer({len(jar)})$ ").strip()
            if not cmd:
                continue

            cmdParts = cmd.split()
            command = cmdParts[0].upper()

            if command in ["NUM", "NUMBER"] and len(cmdParts) == 3:
                result = get_random_number(int(cmdParts[1]), int(cmdParts[2]))
                print(result)
                save2History("number", f"{cmdParts[1]}-{cmdParts[2]}", result)

            elif command == "DICE":
                FACES = int(cmdParts[1]) if len(cmdParts) > 1 else 6
                result = roll_dice(FACES)
                print(result)
                save2History("dice", str(FACES), result)

            elif command == "TIME":
                if len(cmdParts) == 3:
                    result = get_random_time(cmdParts[1], cmdParts[2])
                else:
                    result = get_random_time()
                print(result)
                save2History("time", "", result)

            elif command == "COIN":
                result = flip_coin()
                print(result)
                save2History("coin", "", result)

            elif command == "DATE" and len(cmdParts) == 3:
                result = get_random_date(cmdParts[1], cmdParts[2])
                print(result)
                save2History("date", f"{cmdParts[1]}-{cmdParts[2]}", result)

            elif command == "MIX" and len(cmdParts) > 1:
                items = ' '.join(cmdParts[1:]).split(',')
                result = scramble_list(items)
                print(result)
                save2History("mix", str(items), str(result))

            elif command == "COLOR":
                result = get_random_color()
                print(result)
                save2History("color", "", result)

            elif command == "CARD":
                result = get_random_card()
                print(result)
                save2History("card", "", result)

            elif command == "ELEM":
                result = get_element()
                print(result)
                save2History("element", "", result)

            elif command == "LAND":
                result = get_random_country()
                print(result)
                save2History("country", "", result)

            elif command == "ADD":
                item = ' '.join(cmdParts[1:])
                jar.append(item)
                print(f"ADDED: {item}")

            elif command == "PICK":
                count = int(cmdParts[1]) if len(cmdParts) > 1 else 1
                delay = float(cmdParts[2]) if len(cmdParts) > 2 else 0
                result = pick_from_jar(count, delay)
                if result:
                    print(f"PICKED: {', '.join(result)}")
                else:
                    print("JAR IS EMPTY!")

            elif command == "KEEP":
                saveJar = not saveJar
                print(f"KEEP ITEMS: {'ON' if saveJar else 'OFF'}")

            elif command in ["HIST", "HISTORY"]:
                limit = int(cmdParts[1]) if len(cmdParts) > 1 else 5
                for entry in history[-limit:]:
                    print(f"{entry['when']}: {entry['what']} -> {entry['result']}")

            elif command in ["CLEAR", "CLS"]:
                clear()

            elif command == "HELP":
                print(helpText)

            elif command == "EXIT":
                sys.exit("GOODBYE!")

            else:
                print("UNKNOWN COMMAND! TYPE HELP")

        except Exception as e:
            print(f"ERROR: {str(e)}")

if __name__ == "__main__":
    main()
