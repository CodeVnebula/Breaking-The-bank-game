import os
import time
import sys
from Modules.start import start_game, choices
from Modules.quit_game import quit_play
from Modules.help_sect import help_section

def screen_options():
    option = input(">> ").lower()
# !!!! Need to add an error fixing var
    # after few errors game must be shut down

    while option not in ['play', 'quit', 'help']:    
        option = input(">> ").lower()

    if option == 'play':
       time.sleep(1)
       start_game()
       while retry() == True:
           choices()
    
    elif option == 'help':
        time.sleep(1)
        os.system("cls")
        help_section()
        while back() == True:
            time.sleep(1)
            main_screen()
        
    elif option == 'quit':
        time.sleep(1)
        quit_play()
    
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




def retry():
    print("           / Retry? /          / Quit /", end="\n\n")
   
    which_one = input("'retry' / 'quit' >> ").lower()
    
    while which_one not in ['retry', 'quit']:
        which_one = input("'retry' / 'quit' >> ").lower()
    choose = False
    if which_one == 'retry':
        choose = True
        time.sleep(1)
        os.system("cls")
        
        
    elif which_one == 'quit':
        os.system("cls")
        print(end="\n\n\n")
        print("            Quiting the game... Bye...👋", end="\n\n\n")
        time.sleep(2)
        sys.exit()

    return choose

def back():
    print()
    back = input("'back' >> ").lower()
    isBack = False
    while back != 'back':
        back = input("'back' >> ").lower()
    if back == 'back':
        isBack = True

    return isBack