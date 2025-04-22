import colorama
from colorama import Fore, Style
import time
import os
from os import system

colorama.init(autoreset=True)

def about():
    system("Title: About the Tool")
    print(Fore.CYAN + "This tool is made by: Benny / " + Fore.RED + "---" + Style.RESET_ALL)
    print(Fore.CYAN + "Free Version on https://YOURDISCORDSERVER / " + Fore.RED + "---" + Style.RESET_ALL)
    
    while True:
        back = input(Fore.YELLOW + "Do you want to go back? (y/n): " + Style.RESET_ALL).lower()
        if back == "y":
            time.sleep(0.5)
            return  # ← This will exit the 'about' function and go back to main
        elif back == "n":
            print(Fore.GREEN + "Okay, exiting the tool.")
            time.sleep(1)
            exit()
        else:
            print(Fore.RED + "Invalid choice! Please type 'y' or 'n'.")
            time.sleep(1)

def main():
    print(Fore.CYAN + "This tool is made by: Benny / " + Fore.RED + "---" + Style.RESET_ALL)
    print(Fore.CYAN + "This tool is made for educational purposes only!")
    
    ask = input(Fore.YELLOW + "Do you want to continue? (y/n): " + Style.RESET_ALL).lower()
    
    if ask == "y":
        print(Fore.GREEN + "Starting the tool...")
        time.sleep(2)
        print(Fore.GREEN + "Tool started!")
        time.sleep(2)
        print(Fore.GREEN + "This tool is made for educational purposes only! Enjoy!")
        time.sleep(2)
        print("\nWelcome\n1. About the tool\n2. How to use the tool\n")
        
        choice = input(Fore.YELLOW + "Enter your choice: " + Style.RESET_ALL)
        
        if choice == "1":
            about()
            main()  
        elif choice == "2":
            print(Fore.CYAN + "Usage instructions coming soon!")  # Optional
            time.sleep(2)
            main()
        else:
            print(Fore.RED + "Invalid choice!")
            time.sleep(2)
            main()

    elif ask == "n":
        print(Fore.GREEN + "Exiting the tool. Have a nice day!")
        time.sleep(1)
    else:
        print(Fore.RED + "Invalid choice! Please type 'y' or 'n'.")
        time.sleep(2)
        main()

main()
