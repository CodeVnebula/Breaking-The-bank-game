import time
import os
import sys
from Modules.delay_text_display import print_with_delay
from Modules.Choices.choice_tunnel import tunnel_case
from Modules.Choices.choice_explosion import explosion_case
from Modules.Choices.choice_saw_wall import saw_wall
from Modules.Choices.choice_teleporter import teleport_case
from Modules.Choices.choice_wrecking import wrecking_case
from Modules.Choices.choice_disguise import winning_but_losing_case

with open("Assets/Introduction.txt", "r") as file:
    introduction_text = file.read()

with open("Assets/Mission_telling.txt", "r") as file:
    mission_text = file.read() 

def start_game():
    os.system('cls')
    print("          ", end="")
    
    print_with_delay('Starting the game...')
    time.sleep(2)
    os.system('cls')
    
    print_with_delay("Introduction...") 
    time.sleep(1)
    print()
    
    print_with_delay(introduction_text)
    print("😎", end="\n\n")

    time.sleep(1)
    print_with_delay(mission_text)
    time.sleep(1)
    os.system("cls")
    choices()


def choices():
    print("                 Pick One 👇    ", end="\n\n");
    print(" Tunnel⛏️       Explosion🧨     Saw Wall🪚")
    print(" Wrecking🏗️     Teleporter📟    Disguise💰", end="\n\n")
    print()
    print("Type:  'tunnel'/'explosion'/'saw'/'wrecking'/'teleporter'/'disguise'")
    print()
    choice = input(">> ").lower()
    while choice not in ['tunnel', 'explosion', 'saw', 'wrecking', 'teleporter', 'disguise']:
        choice = input(">> ").lower()
    
    if choice == 'tunnel':
        time.sleep(1)
        os.system("cls")
        tunnel_case()

    elif choice == 'explosion':
        time.sleep(1)
        os.system("cls")
        k = explosion_case()
        while k == True:
            choices()

    elif choice == 'saw':
        time.sleep(1)
        os.system("cls")
        saw_wall()

    elif choice == 'wreckiing':
        time.sleep(1)
        os.system("cls")
        wrecking_case()

    elif choice == 'teleporter':
        time.sleep(1)
        os.system("cls")
        teleport_case()

    elif choice == 'disguise':
        time.sleep(1)
        os.system("cls")
        winning_but_losing_case()
    
    

    


