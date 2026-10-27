#easy linux for ubuntu 0.1.5   
import os

print("WELCOME TO EASYLINUX")
Decision = input("Do you want to continue with the installation? y or N")
print("STARTING THE INSTALLATION, IF YOU WANT TO CANCEL IT PREC CTRL+C")
sleep 
print("if you type n the app won't install and it will pass to the next")
if Decision == "y":
    os.system("sudo apt update && sudo apt upgrade -y")
    print("UPDATING YOUR SYSTEM")

    print("01-> GOOGLE CHROME")
    print("02-> MOZILLA FIREFOX")
    print("03-> BRAVE")
    print("04-> CHROMIUM")
    Navigator = input("WHAT NAVIGATOR WHOULD YOU LIKE TO USE? ")
    if Navigator == "1":
        print("INSTALLING CHROME")
        os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
        os.system("sudo dpkg -i google-chrome-stable_current_amd64.deb")
    if Navigator == "2":
        print("INSTALLING MOZILLA FIREFOX")
        os.system("sudo apt install firefox -y")
    if Navigator == "3":
        print("INSTALLING BRAVE")
        os.system("sudo apt install curl")
        os.system("sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg")
        os.system("echo deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg] https://brave-browser-apt-release.s3.brave.com/ stable main && sudo tee /etc/apt/sources.list.d/brave-browser-release.list")
        os.system("sudo apt-get update -y")
        os.system("sudo apt-get install brave -y")
    if Navigator == "4":
        print("INSTALLING CHROMIUM")
        os.system("sudo apt install chromium -y")
    Dev = input("Do you want to get the dev package")
    if Dev == "y":
        print("INSTALLING PYCHARM")
        os.system("sudo snap install pycharm-community --classic")
        print("INSTALLING GIT")
        os.system("sudo apt install git -y")
        print("INSTALLING VSCODE, THIS MIGHT TAKE A LITTLE LONGER")
        os.system("sudo apt install wget gpg -y &&wget -qO- https://packages.microsoft.com/keys/microsoft.asc | sudo gpg --dearmor -o /usr/share/keyrings/microsoft.gpg")
        os.system("sudo apt update &&sudo apt install code # or code-insiders -y")
    Office = input("DO YOU WANT TO GET THE OFFICE PACKAGE? ")
    if Office == "y":
        print("INSTALLING OFFICE PACKAGE")
        os.system("sudo apt install libreoffice -y")
        os.system("sudo apt-get install slack -y")
    libreoffice = input("Do you want to get libreoffice? (y/N) ")
    if libreoffice == "y":
            print("INSTALLING LIBREOFFICE")
            os.system("sudo apt install libreoffice -y")

    Plasma = input("Do you want to get a desktop enviroment similar to windows (plasma) (y/N) ")
    if Plasma == "y":
        print("INSTALLING KDE PLASMA")
        print("THIS MAY TAKE A LITTLE LONGER")
        os.system("sudo apt install kde-plasma-desktop -y")
    dolphin = input("Do you want to get dolphin (y/N) ")
    if dolphin == "y":
        print("INSTALLING DOLPHIN")
        os.system("sudo apt install dolphin -y")
    studio = input("Do you want to get studio package (y/N) ")
    if studio == "y":
        print("INSTALLING STUDIO PACKAGE")
        os.system("sudo apt install audacity gimp -y")
    spotify = input("Do you want to get spotify (y/N) ")
    if spotify == "y":
        print("INSTALLING SPOTIFY")
        os.system("curl -sS https://download.spotify.com/debian/pubkey_5384CE82BA52C83A.asc | sudo gpg --dearmor --yes -o /etc/apt/trusted.gpg.d/spotify.gpg echo deb https://repository.spotify.com stable non-free | sudo tee /etc/apt/sources.list.d/spotify.list")
        os.system("sudo apt-get update -y && sudo apt-get install spotify-client -y")
    obs = input("Do you want to get obs. An app for recording your screen?")
    if obs == y
        print("INSTALLING OBS-STUDIO")
        os.system("sudo apt install obs-studio -y")

else:
    print("operation cancelled")

print("THANKS FOR USING THE EASY LINUX BETA")
