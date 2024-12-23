from random import randint; import time, os

def clear(): os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear()
    number = randint(-100, 100)
    if (total_guesses := input(r"~\totalGuesses> ")).lower() == "exit" or total_guesses.lower() in ["clear", "cls"]: exit() if total_guesses.lower() == "exit" else clear(); continue
    elif not total_guesses.isdigit(): print("NOT AN INTEGER!!!"); continue
    low, high = -500, 500

    for guess_num in range(1, int(total_guesses) + 1):
        guess = randint(low, high); print(f"Guess {guess_num}: {guess} {'Won!' if guess == number else ''}")
        if guess == number: break
        elif guess > number: high = guess - 1; print("less than that\n")
        else: low = guess + 1; print("more than that\n")
        time.sleep(1)
    else: print("Lost!")
    if input("Again? (Y/n) ").lower() == 'n': break
