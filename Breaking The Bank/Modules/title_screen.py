import os
import time
from Modules.start import start_game, choices

def screen_options():
    option = input(">> ").lower()
# !!!! Need to add an error fixing var
    # after few errors game must be shut down

    while option not in ['play', 'quit']:    
        option = input(">> ").lower()

    if option == 'play':
       time.sleep(1)
       start_game()
       choices()

    
    elif option == 'help':
        #help_section()
        pass
    elif option == 'quit':
        #quit_game()
        pass
    
def main_screen():
    os.system('cls')
    print("#######################")
    print("#  Breaking the Bank  #")
    print("#######################")
    print("        - Play -       ")
    print("        - Help -       ")
    print("        - Quit -       ")
    print("     < 2024 Nexus >    ")
    screen_options()