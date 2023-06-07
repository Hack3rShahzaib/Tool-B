##     Auther   : Shahzaib Arain
##     Tool     : Tool B
##     Language : Python
##     Version  : 0.0.1
##     Githb    : https://github.com/Hack3rShahzaib
##     YouTube  : https://www.youtube.com/channel/UCLHjVvblxo2_XNbwlaRVZ-A
##     Twitter  : https://twitter.com/KingShahza1
##     TikTok   : https://www.tiktok.com/@kingshahzaib85

# Importing some modules
import screen_brightness_control as controllar
import time
import sys
import os

# Color Variable
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'

# Tool Banner
print(f"""{BLUE}
     $$$$$$$$\                 $$\       $$$$$$$\  
    \__$$  __|                 $$ |      $$  __$$\ 
       $$ | $$$$$$\   $$$$$$\  $$ |      $$ |  $$ |
       $$ |$$  __$$\ $$  __$$\ $$ |      $$$$$$$\ |
       $$ |$$ /  $$ |$$ /  $$ |$$ |      $$  __$$\ 
       $$ |$$ |  $$ |$$ |  $$ |$$ |      $$ |  $$ |
       $$ |\$$$$$$  |\$$$$$$  |$$ |      $$$$$$$  |
       \__| \______/  \______/ \__|      \_______/ 
                                               
                {RED}Author : {YELLOW}Shahzaib Arain                                    
                {RED}Github : {MAGENTA}Hack3r Shahzaib                              
        """)
# Welcome message
msg = f"{CYAN}Brightness controllar Created By Shahzaib Arain\n\n"

for shahzaub in msg:
    sys.stdout.write(shahzaub)
    sys.stdout.flush()
    time.sleep(0.1)
# Menus
menu = input(f"""
{GREEN}[1] Check Crount Brightness
{GREEN}[2] Change Brightness
{GREEN}[0] Exit

{CYAN}SELECT OPTION -> {YELLOW}""")
try:
    # if else statement for User Choice
    if menu=="1":
        print(f"{GREEN}Crount Brightness:", MAGENTA, controllar.get_brightness())
        yes_or_no = input(f"\n{CYAN}Do you want to Exit? (y|N) -> {YELLOW}")
        if yes_or_no == "y" or yes_or_no == "Y":
            exit_msg = f"\n{MAGENTA}Thanks For using My Tool Buddy"
            for shahzaub in exit_msg:
                sys.stdout.write(shahzaub)
                sys.stdout.flush()
                time.sleep(0.1)
            exit()
        else:
            os.system("clear")
            os.system("python Brightness_Contrllar.py")
    elif menu=="2":
        brightness = input(f"{CYAN}Enter Brightness -> {YELLOW}")
        controllar.set_brightness(brightness)
        yes_or_no = input(f"\n{CYAN}Do you want to Exit? (y|N) -> {YELLOW}")
        if yes_or_no == "y" or yes_or_no == "Y":
            exit_msg = f"\n{MAGENTA}Thanks For using My Tool Buddy"
            for shahzaub in exit_msg:
                sys.stdout.write(shahzaub)
                sys.stdout.flush()
                time.sleep(0.1)
            exit()
        else:
            os.system("clear")
            os.system("python Brightness_Contrllar.py")
    elif menu=="0":
        exit_msg = f"\n{MAGENTA}Thanks For using My Tool Buddy"
        for shahzaub in exit_msg:
            sys.stdout.write(shahzaub)
            sys.stdout.flush()
            time.sleep(0.1)
        exit()
    else:
        exit()
except:
    exit()