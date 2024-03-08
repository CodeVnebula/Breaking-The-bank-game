import os
import time
from Modules.delay_text_display import print_with_delay

def saw_wall():
    with open("Assets/saw_wall_case.txt", "r") as file:
        saw_wall_story = file.read()

        print_with_delay(saw_wall_story)
        print("🤕")
        time.sleep(2.5)
        os.system("cls")
        print(end="\n\n\n")
        print("                   ❗ F A I L ❗", end="\n\n")
        print("           Wha..? Saw The Wall? Seriously...? 🤦🏻   ", end="\n\n")
        