import os
import platform
import subprocess
from datetime import datetime

def print_info():
    print(f"[{datetime.now().strftime('%H:%M:%S')} - sys info] Retrieving system information...\n")

    print(f"[{datetime.now().strftime('%H:%M:%S')} - sys info] ---------------")
    print(f"[{datetime.now().strftime('%H:%M:%S')} - sys info] Date and Time:")
    print(f"[{datetime.now().strftime('%H:%M:%S')} - sys info] ---------------")
    print(f"[{datetime.now().strftime('%H:%M:%S')} - sys info] Current Date: {datetime.now().strftime('%Y-%m-%d')}")
    print(f"[{datetime.now().strftime('%H:%M:%S')} - sys info] Current Time: {datetime.now().strftime('%H:%M:%S')}\n")

    print(f"[{datetime.now().strftime('%H:%M:%S')} - sys info] ----------------")
    print(f"[{datetime.now().strftime('%H:%M:%S')} - sys info] System Overview:")
    print(f"[{datetime.now().strftime('%H:%M:%S')} - sys info] ----------------")
    print(f"[{datetime.now().strftime('%H:%M:%S')} - sys info] Hostname: {platform.node()}")
    print(f"[{datetime.now().strftime('%H:%M:%S')} - sys info] Operating System: {platform.platform()}")
    print(f"[{datetime.now().strftime('%H:%M:%S')} - sys info] Architecture: {platform.machine()}")
    print(f"[{datetime.now().strftime('%H:%M:%S')} - sys info] Processor(s): {platform.processor()}")
    boot_time = subprocess.check_output("systeminfo | findstr /C:'System Boot Time'", shell=True).decode().strip()
    print(f"[{datetime.now().strftime('%H:%M:%S')} - sys info] System Uptime: {boot_time.split(':', 1)[1].strip()}\n")

    print(f"[{datetime.now().strftime('%H:%M:%S')} - sys info] ---------------------")
    print(f"[{datetime.now().strftime('%H:%M:%S')} - sys info] Hardware Information:")
    print(f"[{datetime.now().strftime('%H:%M:%S')} - sys info] ---------------------")
    print(f"[{datetime.now().strftime('%H:%M:%S')} - sys info] CPU(s):")
    print(subprocess.check_output("wmic cpu get name, maxclockspeed, numberofcores", shell=True).decode().strip())
    print(f"[{datetime.now().strftime('%H:%M:%S')} - sys info] Memory:")
    print(subprocess.check_output("wmic memorychip get capacity, speed", shell=True).decode().strip())
    print(f"[{datetime.now().strftime('%H:%M:%S')} - sys info] Disk(s):")
    print(subprocess.check_output("wmic diskdrive get caption, size", shell=True).decode().strip())

    print(f"[{datetime.now().strftime('%H:%M:%S')} - sys info] ----------------")
    print(f"[{datetime.now().strftime('%H:%M:%S')} - sys info] Network Details:")
    print(f"[{datetime.now().strftime('%H:%M:%S')} - sys info] ----------------")
    print(subprocess.check_output("ipconfig | findstr IPv4", shell=True).decode().strip())

    print(f"[{datetime.now().strftime('%H:%M:%S')} - sys info] -------------------")
    print(f"[{datetime.now().strftime('%H:%M:%S')} - sys info] Software Installed:")
    print(f"[{datetime.now().strftime('%H:%M:%S')} - sys info] -------------------")
    print(subprocess.check_output("wmic product get name, version", shell=True).decode().strip())

    print(f"[{datetime.now().strftime('%H:%M:%S')} - sys info] -------------------")
    print(f"[{datetime.now().strftime('%H:%M:%S')} - sys info] Running Processes:")
    print(f"[{datetime.now().strftime('%H:%M:%S')} - sys info] -------------------")
    print(subprocess.check_output("tasklist", shell=True).decode().strip())


# Main
print("  _  _ ___ _    ___  _____   __")
print(" | || | __| |  |   \| __\ \ / /")
print(" | __ | _|| |__| |) | _| \ V / ")
print(" |_||_|___|____|___/|___| \_/  ")
print("\n####################################")
print("#                                  #")
print("# Welcome to Heldev Corporation!   #")
print("#                                  #")
print("# System Information Tool v1.0     #")
print("#                                  #")
print("####################################\n")
print_info()
os.system("./main.py")
