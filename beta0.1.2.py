#easy linux for ubuntu
import os

print("WELCOME TO EASYLINUX")
Decision = input("Do you want to continue with the installation? y or N")
if Decision == "y":
    os.system("sudo apt update && sudo apt upgrade")
    print("UPDATING YOUR SYSTEM")

            Navigator = input("WHAT NAVIGATOR WHOULD YOU USE")
            print("01-> GOOGLE CHROME")
            print("02-> MOZILLA FIREFOX")
            print("03-> brave")
            print("04-> CHROMIUM")
            if navigator == "1":
                print("INSTALLING CHROME")
                os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
                os.system("sudo dpkg -i google-chrome-stable_current_amd64.deb")
            if Navigator == "2":
                print("INSTALLING MOZILLA FIREFOX")
                    os.system("sudo apt install firefox")
            if Navigator == "3":
                print("INSTALLING BRAVE")
                os.system("sudo apt install curl")
                os.system("sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg")
                os.system("echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg] https://brave-browser-apt-release.s3.brave.com/ stable main" | sudo tee /etc/apt/sources.list.d/brave-browser-release.list")
                os.system("sudo apt-get update")
                os.system("sudo apt-get install brave")
            if Navigator == "4":
                print("INSTALLING CHROMIUM")
                os,system("sudo apt install chromium")
            Office == input("DO YOU WANT TO GET THE OFFICE PACKAGE?")
            if Office == "y":
                print("INSTALLING OFFICE PACKAGE")
                os.system("sudo apt install libreoffice")
                os.system("sudo apt-get install slack")
            libreoffice = input("Do you want to get libreoffice? (y/N) ")
                if libreoffice == "y":
                    print("INSTALLING LIBREOFFICE")
                    os.system("sudo apt install libreoffice")

            Plasma = input("Do you want to get a desktop enviroment similar to windows (plasma) (y/N) ")
            if Plasma == "y":
                print("INSTALLING KDE PLASMA")
                print("THIS MAY TAKE A LITTLE LONGER")
                os.system("sudo apt install kde-plasma-desktop")
            dolphin = input("Do you want to get dolphin (y/N) ")
            if dolphin == "y":
                print("INSTALLING DOLPHIN")
                os.system("sudo apt install dolphin")
            studio = input("Do you want to get studio package (y/N) ")
            if studio == "y":
                print("INSTALLING STUDIO PACKAGE")
                os.system("sudo apt install audacity gimp")
            spotify = input("Do you want to get spotify (y/N) ")
            if spotify == "y":
                print("INSTALLING SPOTIFY")
                os.system("curl -sS https://download.spotify.com/debian/pubkey_5384CE82BA52C83A.asc | sudo gpg --dearmor --yes -o /etc/apt/trusted.gpg.d/spotify.gpg echo "deb https://repository.spotify.com stable non-free" | sudo tee /etc/apt/sources.list.d/spotify.list")
                os.system("sudo apt-get update && sudo apt-get install spotify-client")
        else:
            print("operation cancelled")

        print("THANKS FOR USING THE EASY LINUX BETA")