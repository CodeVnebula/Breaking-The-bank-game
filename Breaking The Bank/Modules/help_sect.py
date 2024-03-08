from Modules.delay_text_display import print_with_delay

def help_section():
    with open("Assets/help.txt", "r") as file:
        _help = file.read() 

        print_with_delay(_help)


    