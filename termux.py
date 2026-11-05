#easy linux 'termux' beta 0.1.1
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

proot = input("DO YOU WANT TO GET PROOT-DISTRO? ")
if proot == "Y":
    os.system("pkg install proot-distro -y")
    print("proot-distro installed correctly")
    time.sleep(3)
    distro = input("what distro do you want: 
          1 =>Ubuntu
          2 =>Arch
          3 =>Fedora
          4 =>Alpine")
    if distro == "1":
        print("installing ubuntu:24.04")
        os.system("proot-distro install ubuntu:24.04")
        print("INSTALLED CORRECTLY")
        time.sleep(5)

    if distro == "2":
        print("INSTALLING ARCH LINUX")
        os.system("proot-distro install archlinux:latest")
        print ("INSTALLED CORRECTLY")
        time.sleep(5)

    if distro == "3":
        print("INSTALLING FEDORA")
        os.system("proot-distro install fedora:latest")
        print("INSTALLED CORRECTLY")
        time.sleep(5)

    if distro == "4":
        print("INSTALLING ALPINE")
        os.system("proot-distro install alpine:latest")
        print("INSTALLED CORRECTLY")
        time.sleep(5)

gpg = input("DO YOU WANT TO GET GNUPG? ")
if gpg =="y":
    print("INSTALLING GNUPG")
    os.system("pkg install gnupg")
    print("INSTALLED CORRECTLY")
    time.sleep(5)

ssh = input("DO YOU WANT TO GET SSH CLIENT? ")
if ssh == "y":
    print("INSTALLING SSH CLIENT")
    os.system("pkg install ssh")
    print("INSTALLED CORRECTLY")
    time.sleep(5)
    
