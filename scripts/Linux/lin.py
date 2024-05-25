import os

def scan_network():
    target_ip = input("Enter the target IP/subnet: ")
    os.system(f"./scripts/Linux/network_scan.sh {target_ip}")


def scan_ports():
    target_ip = input("Enter the target IP: ")
    os.system(f"./scripts/Linux/port_scan.sh {target_ip}")


def analyze_vulnerabilities():
    target_ip = input("Enter the target IP: ")
    os.system(f"./scripts/Linux/vuln_scan.sh {target_ip}")


def get_info():
    os.system("python ./scripts/getinfo.py")

def main():
    while True:
        print("\nCybersecurity Tool (Linux/macOS)")
        print("1. Network Scan")
        print("2. Port Scan")
        print("3. Vulnerability Analysis")
        print("4. Systeme information")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            scan_network()
        elif choice == '2':
            scan_ports()
        elif choice == '3':
            analyze_vulnerabilities()
        elif choice == '4':
            get_info()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
