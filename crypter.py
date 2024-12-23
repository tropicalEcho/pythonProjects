import string, random, os

chars = list(string.ascii_letters + string.digits + string.punctuation + " ")
shuffled = chars.copy()
random.shuffle(shuffled)
cipher = dict(zip(chars, shuffled))

messages = {}
used_codes = set()

def clear(): os.system("cls" if os.name == "nt" else "clear")

def showEm():
    for key, value in cipher.items():
        print(f"{key} : {value}")

def thePassword():
    while True:
        code = str(random.randint(1000, 9999))
        if code not in used_codes:
            used_codes.add(code)
            return code

def encrypt(message):
    encrypted = ""
    for char in message:
        encrypted += cipher.get(char, char)
    
    code = thePassword()
    messages[code] = encrypted
    return code

def decrypt(code):
    if code in messages:
        message = messages[code]
        reverse_cipher = {v: k for k, v in cipher.items()}
        decrypted = ""
        for char in message:
            decrypted += reverse_cipher.get(char, char)
        return f"Decrypted: {decrypted}"
    return "Wrong code!"

while True:
    cmd = input("~$ ").strip()
    
    if cmd.lower() == "exit":
        print("Goodbye!")
        break
    elif cmd.lower() == "clear":
        clear()
    elif cmd.lower() == "showem":
        showEm()
    elif cmd.lower().startswith("decrypt "):
        print(decrypt(cmd[8:]))
    else:
        print(f"Code: {encrypt(cmd)}")
