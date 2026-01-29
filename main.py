import os
from colorama import Fore, Back, Style, init
from tutor_logic import PythonTutor

init(autoreset=True)

def main():
    try:
        tutor = PythonTutor()
    except Exception as e:
        print(Fore.RED + f"Configuration Error: {e}")
        return

    os.system('clear')
    
    # UI Header
    print(Fore.BLUE + "┌" + "─" * 58 + "┐")
    print(Fore.BLUE + "│ " + Fore.CYAN + "      BIT | SENIOR PYTHON MENTOR - LOCAL AI        " + Fore.BLUE + " │")
    print(Fore.BLUE + "└" + "─" * 58 + "┘")
    print(Fore.WHITE + Style.DIM + " Commands: 'exit' to quit | 'clear' to reset screen | 'save' to export\n")

    while True:
        try:
            user_input = input(Fore.YELLOW + "Student ❯ " + Style.RESET_ALL).strip()

            if user_input.lower() in ['exit', 'quit', 'bye']:
                print(Fore.BLUE + "\nBit: See you in the next debugging session. Happy coding!")
                break
                
            if user_input.lower() == 'clear':
                os.system('clear')
                continue

            if not user_input:
                continue

            # Visual thinking state
            print(Fore.BLACK + Back.CYAN + " BIT IS THINKING... " + Style.RESET_ALL, end="\r")
            
            response = tutor.send_message(user_input)
            
            # Clear "thinking" line
            print(" " * 40, end="\r")
            
            # Message Design
            print(Fore.BLUE + "╭" + "─" * 5)
            print(Fore.BLUE + "│ " + Fore.GREEN + Style.BRIGHT + "BIT SAYS:")
            
            for line in response.split('\n'):
                # Handle empty lines for better spacing
                line_content = line if line.strip() else ""
                print(Fore.BLUE + "│ " + Fore.WHITE + line_content)
            
            print(Fore.BLUE + "╰" + "─" * 5 + "\n")
            
        except KeyboardInterrupt:
            print(Fore.YELLOW + "\n\nSession terminated by user.")
            break
        except Exception as e:
            print(Fore.RED + f"\n[!] System Error: {e}")

if __name__ == "__main__":
    main()
