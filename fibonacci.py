import os

def clear(): os.system("cls" if os.name == "nt" else "clear")

def calculate_fibonacci(n, sequence):
    while len(sequence) <= n: sequence.append(sequence[-1] + sequence[-2])
    return sequence[n]

def main():

    fibonacci_sequence = [0, 1]
    clear()

    while True:
        try:
            cmd = input(r".\Fibonacci> ").lower().strip()
            
            if cmd in ["cls", "clean", "clear"]: clear(); continue
            elif cmd == "exit": print("Goodbye!"); break
            elif cmd == "help": print("Enter a number to get Fibonacci on that position\n'clear' to clear screen\n'show' to display current sequence\n'exit' to quit"); continue
            elif cmd == "show": print(f"\nCurrent sequence: {fibonacci_sequence}"); continue

            if cmd.isdigit():
                n = int(cmd)
                if n < 0: print("Please enter a non-negative number."); continue  
                print(f"\nF({n}) = {calculate_fibonacci(n, fibonacci_sequence)}")
            else: print("\nInvalid input. Type 'help' for commands.")
                
        except KeyboardInterrupt: print("\nGoodbye!"); break
        except Exception as e: print(f"\nAn error occurred: {str(e)}")

if __name__ == "__main__": main()