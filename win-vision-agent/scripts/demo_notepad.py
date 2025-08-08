import time, os, pyautogui as pag
from utils.vision import find_on_screen

def main():
    # Open Notepad
    pag.hotkey("win", "r")
    time.sleep(0.4)
    pag.typewrite("notepad\n")
    time.sleep(0.6)

    # Type text
    pag.typewrite("Hello from win-vision-agent\n")
    time.sleep(0.2)

    # Save file
    pag.hotkey("ctrl", "s")
    time.sleep(0.4)
    pag.typewrite("demo.txt\n")

if __name__ == "__main__":
    main()
