#easy linux for ubuntu
import os
print("WELCOME TO EASYLINUX")
Decision = input("Do you want to continue with the installation? y or N")
if Decision == "y":
    os.system("sudo apt update && sudo apt upgrade")
    print("UPDATING YOUR SYSTEM")

    libreoffice = input("Do you want to get libreoffice? (y/N) ")
    if libreoffice == "y":
        os.system("sudo apt install libreoffice")

    Plasma = input("Do you want to get a desktop enviroment similar to windows (plasma) (y/N) ")
    if Plasma == "y":
        os.system("sudo apt install kde-plasma-desktop")
    Chrome = input("will you use google chrome (y/N) ")
    if Chrome == "y":
        os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
        os.system("sudo dpkg -i google-chrome-stable_current_amd64.deb")
    dolphin = input("Do you want to get dolphin (y/N) ")
    if dolphin == "y":
        os.system("sudo apt install dolphin")
    studio = input("Do you want to get studio package (y/N) ")
    if studio == "y":
        os.system("sudo apt install audacity gimp")
else:
    print("operation cancelled")

print("THANKS FOR USING THE EASY LINUX BETA")