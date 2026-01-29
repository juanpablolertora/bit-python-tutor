import os
from colorama import Fore, Back, Style, init
from tutor_logic import PythonTutor

init(autoreset=True)

def main():
    try:
        tutor = PythonTutor()
    except Exception as e:
        print(Fore.RED + f"Error de configuración: {e}")
        return

    os.system('clear')
    
    print(Fore.BLUE + "┌" + "─" * 58 + "┐")
    print(Fore.BLUE + "│ " + Fore.CYAN + "      BIT | PYTHON MENTOR & CODE ANALYZER         " + Fore.BLUE + " │")
    print(Fore.BLUE + "└" + "─" * 58 + "┘")
    print(Fore.WHITE + Style.DIM + " Comandos: 'exit' para salir | 'clear' para limpiar pantalla\n")

    while True:
        try:
            user_input = input(Fore.YELLOW + "User ❯ " + Style.RESET_ALL).strip()

            if user_input.lower() in ['exit', 'quit', 'bye']:
                print(Fore.BLUE + "\nBit: Estaré aquí cuando el código falle. ¡Adiós!")
                break
                
            if user_input.lower() == 'clear':
                os.system('clear')
                continue

            if not user_input:
                continue

            print(Fore.BLACK + Back.BLUE + " BIT ESTÁ PENSANDO... " + Style.RESET_ALL, end="\r")
            
            response = tutor.send_message(user_input)
            
            # Limpiar la línea de "pensando"
            print(" " * 30, end="\r")
            
            # Diseño de respuesta
            print(Fore.BLUE + "╭" + "─" * 4)
            print(Fore.BLUE + "│ " + Fore.GREEN + "BIT:")
            
            for line in response.split('\n'):
                print(Fore.BLUE + "│ " + Fore.WHITE + line)
            
            print(Fore.BLUE + "╰" + "─" * 4 + "\n")
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(Fore.RED + f"\n[!] Error en el sistema: {e}")

if __name__ == "__main__":
    main()
