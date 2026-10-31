#easy linux 'termux' beta 0.1
import os
import time


print("UPDATING THE SISTEM")
os.system("pkg update -y")
print("UPGRADING THE SYSTEM PACKAGES")
os.system("pkg upgrade")
os.system("apt autoremove")
print("EVERYTHING UPDATED CORRECTLY")
time.sleep(5)

cctv = input("DO YOU WANT TO GET A CAMERA HACKING TOOL? ")
if cctv == "y":
    os.system("git clone https://github.com/mohammadmahdi-termux/hackCCTV")
    print("INSTALLED CORRECTLY. YOU WILL FIND IT ON A FOLDER NAMED 'HACKcctv'")
    time.sleep(5)

nano = input("DO YOU WANT TO GET NANO?. AN SIMPLE TEDT EDITO")
if nano == "y":
    os.system("apt install nano")
    print("INSTALLED CORRECTLY")
    time.sleep(5)

nvim = input("DO YOU WANT TO GET NVIM?. IT IS AN ADVANCED TEXT EDITOR")
if nvim == "y":
    os.system("pkg install neovim")
    print("INSTALLED CORRECTLY, TO EXEC IT JUST TYPE 'nvim'")
    time.sleep(5)

zsh = input("DO YOU WANT TO GET A BETTER SHELL 'ZSH'? ")
if zsh == "y":
    os.system("apt install zsh")
    print("INSTALLED CORRECTLY, SETTING IT AS YOUR DEFAULT SHELL")
    time.sleep(5)
    os.system("chsh /bin/zsh")
    print("CORRECTLY APLIED")
    time.sleep(5)
