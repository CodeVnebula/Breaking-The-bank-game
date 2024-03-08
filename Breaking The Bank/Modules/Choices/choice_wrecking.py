import os
import time
from Modules.delay_text_display import print_with_delay


def wrecking_case():
    with open("Assets/wrecking_ball_case.txt", "r") as file:
        ball_story = file.read()

        print_with_delay(ball_story)
        print("🤕")
        time.sleep(2.5)
        os.system("cls")
        print(end="\n\n\n")
        print("                   ❗ F A I L ❗", end="\n\n")
        print("         No Construction work scheduled for today!    ", end="\n\n")
        