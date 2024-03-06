import time

def print_with_delay(text, delay=0.055):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)


