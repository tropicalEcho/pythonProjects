import string, random, sys, os

isDone = False

def clear():
    os.system("cls" if os.name == "nt" else "clear")

chars = list(string.ascii_letters + string.digits + string.punctuation + " ")
shuffled = chars.copy()
random.shuffle(shuffled)
cipher = dict(zip(chars, shuffled))

def showEm():
    for key, value in cipher.items():
        print(f"{key} : {value}")

def encrypt(message):
    newMessage = ""
    for char in message:
        if char in cipher: newMessage += cipher[char]
        else: newMessage += char
    codes = ("Fahrenheit", "SpiderMan", "JamesBond", "Jackson", "ElviS", "Ground Control")
    code = random.choice(codes)
    isDone = True
    return code 

def decrypt(code):
    global newMessage
    if isDone and code == newMessage:



while True:
    cmd = input("~$ ")
    if cmd.lower() == "exit": sys.exit("Goodbye!")
    elif cmd.lower() == "clear": clear()
    elif cmd == "showEm": showEm()
    else: print(f"Key: {encrypt(cmd)}")
