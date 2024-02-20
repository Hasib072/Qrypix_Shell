
import keyboard
import os
import time
import sys
import mimetypes
from colorama import init, Fore, Style

init(autoreset=True)

def loading_bar(text="Loading", duration=5, width=30):
    """
    Displays a loading bar in the console.

    Parameters:
    - duration: The total time in seconds for the loading to complete.
    - width: The width of the loading bar in characters.
    """
    print("Loading:", end=" ")
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        percent_complete = elapsed_time / duration
        bar_length = int(percent_complete * width)
        bar = "█" * bar_length + " " * (width - bar_length)
        print(Fore.GREEN + Style.BRIGHT + f"\r{text} {bar} {int(percent_complete * 100)}%", end="")
        sys.stdout.flush()
        if elapsed_time >= duration:
            break
        time.sleep(0.1)  # Update every 0.1 seconds
    print("\n")
    print(Fore.GREEN + Style.BRIGHT +  f"{text} complete!")

def set_console_window_size(width, height):
    """Sets the console window size."""
    command = f'mode con: cols={width} lines={height}'
    os.system(command)


def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_ASCII_logo():
    print(Fore.GREEN + Style.BRIGHT + r"""
         ██████╗ ██████╗ ██╗   ██╗██████╗ ████████╗██╗██╗  ██╗
        ██╔═══██╗██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██║╚██╗██╔╝
        ██║   ██║██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║ ╚███╔╝ 
        ██║▄▄ ██║██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║ ██╔██╗ 
        ╚██████╔╝██║  ██║   ██║   ██║        ██║   ██║██╔╝ ██╗
         ╚══▀▀═╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝   ╚═╝╚═╝  ╚═╝
                                                    ©NexZLabs             
    """)

def display_menu(current_selection, menu_items):
    """Displays the menu with the current selection highlighted."""
    clear_screen()
    print_ASCII_logo()
    for i, option in enumerate(menu_items):
        if i == current_selection:
            print(Fore.RED + Style.BRIGHT +  f"> {option}")
        else:
            print(f"  {option}")

def PressEnterkey():
    input("\nPress enter to continue...")
    time.sleep(0.1)

def is_valid_text_file(file_path):
    """
    Validates that the file exists and is a text file.

    Parameters:
    - file_path: The path to the file to validate.

    Returns:
    - True if the file exists and is a text file, False otherwise.
    """
    # Check if the file exists
    if not os.path.isfile(file_path):
        print("The file does not exist.")
        return False

    # Guess the type of the file based on its extension
    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type is None:
        print("Could not determine the file type.")
        return False

    # Check if the guessed MIME type starts with 'text/'
    if mime_type.startswith('text/'):
        return True
    else:
        print("The file is not a text file.")
        return False

def say_hi():
    """Asks for the user's name and prints a greeting."""
    clear_screen()
    print_ASCII_logo()
    file_path = input("Enter the Path of File to Encrypt: ")
    oputputloc = input("Enter the Path for Output File: ")
    print(" ")
    if is_valid_text_file(file_path):
        loading_bar("Encrypting",duration=10, width=30)
        print(f"Encrypted File Saved in {oputputloc}!")
        time.sleep(1.0)
    else:
        print("The file is not valid or not a text file.")
    

def main():
    # Menu items
    
    # Set the console window size as soon as the program starts
    # if os.name == 'nt':  # Only attempt to set console size on Windows
    #     set_console_window_size(80, 25)  # Adjust these values as needed
        

    menu_items = ["1. Encrypt File", "2. Decrypt File", "3. How to Use", "4. About Us", "5. Exit"]
    current_selection = 0

    # Initial display
    display_menu(current_selection, menu_items)

    # Main loop
    running = True
                                
    while running:
        time.sleep(0.1)
        if keyboard.is_pressed('up') and current_selection > 0:
            current_selection -= 1
            display_menu(current_selection, menu_items)
            time.sleep(0.2) # Prevents overly rapid selection changes
        elif keyboard.is_pressed('down') and current_selection < len(menu_items) - 1:
            current_selection += 1
            display_menu(current_selection, menu_items)
            time.sleep(0.2) # Prevents overly rapid selection changes
        elif keyboard.is_pressed('enter'):
            if current_selection == 0: # Say Hi selected
                PressEnterkey()
                say_hi()
                PressEnterkey()
                display_menu(current_selection, menu_items)
            elif current_selection == 1:
                PressEnterkey()
                print("OHOHOHOHO!")
                PressEnterkey()
                display_menu(current_selection, menu_items)
            elif current_selection == len(menu_items) - 1: # Exit selected
                running = False
            else:
                clear_screen()
                print(f"You selected {menu_items[current_selection]}")
                PressEnterkey()
                display_menu(current_selection, menu_items)

    print("Exiting...")

if __name__ == "__main__":
    main()
