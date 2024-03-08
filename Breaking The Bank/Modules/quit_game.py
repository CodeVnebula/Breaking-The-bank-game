import os
import time
import sys
from Modules.delay_text_display import print_with_delay

def quit_play():
    os.system("cls")
    
    print_with_delay(">>> Quiting the game... Bye...👋")
    time.sleep(1)
    print()
    print_with_delay(">>> Wait...Sure you want to quit?")
    print()

    yes_no = input("[yes/no] >> ").lower()

    while yes_no not in ['yes', 'no']:
        yes_no = input("[yes/no] >> ").lower()

    if yes_no == "yes":
        print()
        print_with_delay(">>> Going back to main menu")
        time.sleep(2)
        print()
        print_with_delay(">>> Ughh...Looks like My code Misunderstood the task😅")
        print()
        time.sleep(2)
        print_with_delay(">>> Ok, ok, Just kidding🤪... now quiting... Really😁")
        time.sleep(1)
        sys.exit()

    elif yes_no == 'no':
        time.sleep(1)
        print_with_delay(">>> Then why did you choose quit before?🤔")
        print()
        time.sleep(2)
        print_with_delay(">>> Ok...😕 Bye")
        time.sleep(1)
        sys.exit()
