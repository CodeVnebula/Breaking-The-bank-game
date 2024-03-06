import os
import time
from Modules.delay_text_display import print_with_delay
from Modules.retry_options import retry

def explosion_case():
    with open("Assets/explosive.txt", "r") as file:
        explosion_story = file.read()

        print_with_delay(explosion_story)
        print("🤕")
        time.sleep(2.5)
        os.system("cls")
        print(end="\n\n\n")
        print("                   ❗ F A I L ❗", end="\n\n")
        print("              Worst Way to Learn Flying😂    ", end="\n\n")
        retry()