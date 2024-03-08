import os
import time
from Modules.delay_text_display import print_with_delay

def teleport_case():
    with open("Assets/teleporter_case.txt", "r") as file:
        teleport_story = file.read()

        print_with_delay(teleport_story)
        print("🤕")
        time.sleep(2.5)
        os.system("cls")
        print(end="\n\n\n")
        print("                   ❗ F A I L ❗", end="\n\n")
        print("             I also tought it would Work🤷🏽    ", end="\n\n")
        