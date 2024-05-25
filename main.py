import platform
import os
import subprocess
import urllib.request
from datetime import datetime


def install_dependencies():
    os_type = platform.system()
    if os_type == "Linux" or os_type == "Darwin":
        os.system("sudo apt-get install nmap -y")
    elif os_type == "Windows":
        nmap_url = "https://nmap.org/dist/nmap-7.91-setup.exe"
        nmap_installer = "nmap_setup.exe"
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Downloading Nmap installer for Windows...")
        urllib.request.urlretrieve(nmap_url, nmap_installer)
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Installing Nmap for Windows...")
        os.system(nmap_installer)
        add_nmap_to_path()
def add_nmap_to_path():
    nmap_path = r"C:\Program Files (x86)\Nmap"
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Adding Nmap to PATH...")
    current_path = os.environ.get('PATH')
    if nmap_path not in current_path:
        new_path = current_path + ";" + nmap_path
        os.environ['PATH'] = new_path
        subprocess.run(['setx', 'PATH', new_path])
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Nmap added to PATH.")


def what_os():
    os_type = platform.system()
    if os_type == "Linux" or os_type == "Darwin":
        os.system("python3 scripts/Linux/lin.py")
    elif os_type == "Windows":
        os.system("python scripts/Windows/win.py")
    else:
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Unsupported operating system.")


def language(lg):
    def french():
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Vous avez choisi la langue française")
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Détermination du système d'exploitation")
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Ouverture du programme correspondant")
        what_os()

    def english():
        print(f"[{datetime.now().strftime('%H:%M:%S')}] You chose English language")
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Determining operating system")
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Opening the corresponding program")
        what_os()

    if lg == 1:
        french()
    elif lg == 2:
        english()
    else:
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Error: Invalid language choice")


def main():
    print("  _  _     ___      __    _ _ \n"
          " | || |___| \\ \\    / /_ _| | |\n"
          " | __ / -_) |\\ \\/\\/ / _` | | |\n"
          " |_||_\\___|_| \\_/\\_/\\__,_|_|_|")

    print("######################\n"
          "# SECURITY OPERATING #\n"
          "#    Applications    #\n"
          "######################")

    lang = int(input("Choose language: [1 - French] [2 - English]: "))
    install_dependencies()
    language(lang)


if __name__ == "__main__":
    main()
