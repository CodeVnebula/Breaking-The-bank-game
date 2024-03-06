import os
import time
from Modules.delay_text_display import print_with_delay
from Modules.retry_options import retry


def tunnel_case():
    with open("Assets/tunnel.txt", "r") as file:
        tunnel_story = file.read()

        print_with_delay(tunnel_story)
        print("😵")
        time.sleep(2.5)
        os.system("cls")
        print(end="\n\n\n")
        print("                  ❗ F A I L ❗", end="\n\n")
        print("              Wth Where You Thinking🧐    ", end="\n\n")
        retry()
