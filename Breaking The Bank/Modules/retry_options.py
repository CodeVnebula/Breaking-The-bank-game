import time
import sys
import os

def retry():
    print("/ Retry? /          / Quit /")
    which_one = input(">> ").lower()

    while which_one not in ['retry', 'quit']:
        which_one = input(">> ").lower()
    if which_one == 'retry':
        time.sleep(1)
        os.system("cls")
    elif which_one == 'quit':
        print("Quiting the game. Bye...👋", end="\n\n")
        time.sleep(2)
        sys.exit()
        
