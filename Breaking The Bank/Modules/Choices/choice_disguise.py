import os
import time
from Modules.delay_text_display import print_with_delay
from Modules.quit_game import quit_play

def winning_but_losing_case():
    with open("Assets/disguise_last_case.txt", "r") as file:
        end_story = file.read()

        print_with_delay(end_story)
        print("🤕")
        time.sleep(3)
        os.system("cls")
        print(end="\n\n\n")
        print("                      CAN't SAY IT's A")
        print("                             FAIL     ")
        print("                          BUT IT's    ")
        print("                          NOT A WIN   ")
        print(" Play our(Not our idea) next Part of the Game for more Sticky Stories 🙂🤪 ", end="\n\n")
        
        print("Quit Game? ", end="\n\n")
        _quit = input(" 'quit' >> ").lower()

        while _quit != 'quit':
            _quit = input(" 'quit' >> ").lower()

        if _quit == 'quit':
            quit_play()
        