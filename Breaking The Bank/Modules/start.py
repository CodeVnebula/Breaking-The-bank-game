import time
import os
from Modules.delay_text_display import print_with_delay
from Modules.Choices.choice_tunnel import tunnel_case
from Modules.Choices.choice_explosion import explosion_case


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
    

def choices():
    print("                 Pick One 👇    ", end="\n\n");
    print(" Tunnel⛏️       Explosion🧨     Saw Wall🪚")
    print(" Wrecking🏗️     Teleporter📟    Disguise💰", end="\n\n")

    choice = input(">> ").lower()
    while choice not in ['tunnel', 'explosion', 'saw wall', 'wreckiing', 'teleporter', 'disguise']:
        choice = input(">> ").lower()
    
    if choice == 'tunnel':
        time.sleep(1)
        os.system("cls")
        tunnel_case()
    elif choice == 'explosion':
        time.sleep(1)
        os.system("cls")
        explosion_case()
    elif choice == 'saw wall':
        time.sleep(1)
        os.system("cls")
        pass
    elif choice == 'wreckiing':
        time.sleep(1)
        os.system("cls")
        pass
    elif choice == 'teleporter':
        time.sleep(1)
        os.system("cls")
        pass
    elif choice == 'disguise':
        time.sleep(1)
        os.system("cls")
        pass


    


