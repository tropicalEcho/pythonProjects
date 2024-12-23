import random, shlex
from os import name, system

# Character sets
symbols = "!@#$%^&*()_-+={}[]|:;'\"<>?.~/`"
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"

def clear():
    system("cls" if name == "nt" else "clear")

def helper():
    print("""
Commands:
check <password> - Check password strength
gen <length> sym/let/dig - Generate password (use sym/let/dig for types)
clear - Clear screen
help - Show this message
exit - Exit program
    """)

def check_pass_strength(password):
    score = 0
    
    # Check length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    
    # Check character types
    if any(c in symbols for c in password): score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.islower() for c in password): score += 1
    if any(c in digits for c in password): score += 1

    # Return strength
    if score >= 5: return "Strong"
    elif score >= 3: return "Moderate"
    elif score >= 2: return "Fair"
    return "Weak"

def generate_password(length, sym, let, dig):
    if length < 1:
        return "Error: Length too short"
    
    chars = ""
    if sym: chars += symbols
    if let: chars += letters
    if dig: chars += digits
    
    if not chars:
        return "Error: Select at least one character type"
    
    password = ''.join(random.choice(chars) for _ in range(length))
    return f"Your Password: {password}\nStrength: {check_pass_strength(password)}"

def main():
    clear()
    helper()
    while True:
        try:
            cmd = shlex.split(input("~$ ").lower())
            
            if cmd[0] in ["check", "stren", "rate"] and len(cmd) == 2:
                print(check_pass_strength(cmd[1]))
                
            elif cmd[0] in ["gen", "new"] and len(cmd) >= 2:
                if cmd[1].isdigit():
                    print(generate_password(int(cmd[1]), "sym" in cmd, "let" in cmd, "dig" in cmd))
                else: 
                    print("Error: Length must be a number")
                    
            elif cmd[0] in ["exit", "quit"]:
                break
                
            elif cmd[0] in ["clear", "cls"]:
                clear()
                
            elif cmd[0] in ["help", "h"]:
                helper()
                
            else:
                print("Invalid command")
                
        except Exception as e:
            print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()