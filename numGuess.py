from sys import exit
from random import randint

try: 
    number = randint(int(input("INITAL: ")), int(input("FINAL: ")))
except ValueError: 
    print("ERROR!")
    exit("GOODBYE!")

while True:
    try: 
        totalGuesses = int(input("HOW MANY CHANCES? [1, 25]: "))
        if 1 <= totalGuesses <= 25: 
            break
    except ValueError: 
        print("ERROR!")

for guesses in range(1, totalGuesses + 1):
    try: 
        guess = int(input(f"Guess {guesses}: "))
    except: 
        print("ERROR!")
        exit("GOODBYE!")

    if guess == 0: 
        print(f"NUMBER: {number}")
        break
    elif guess == number: 
        print("YOU WON!")
        break
    elif guess > number: 
        print("SOMETHIN' LESS")
    else: 
        print("SOMTHIN' MORE")
else: 
    print("YOU LOST!")
