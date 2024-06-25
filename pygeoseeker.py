import os
import sys
import time
import platform
import subprocess
import ipinfo


class PyGeoSeeker:

    """SET-UP"""
    def __init__(self):
        self.os_name = platform.system()
        self.requirements = [
            'ipinfo',
            'pyfiglet',
            'termcolor',
            'colorama']
        self.install_missing_packages(self.requirements)
        self.main()
    
    @staticmethod
    def is_package_installed(package_name):
        try:
            import importlib
            importlib.import_module(package_name)
            return True
        except ImportError:
            return False

    def install_missing_packages(self, packages):
        checkmark = '\u2713'

        try:
            if self.os_name == 'Windows':
                missing_packages = [pkg for pkg in packages if not self.is_package_installed(pkg)]

                if missing_packages:
                    print(f"Installing missing packages: {', '.join(missing_packages)}")
                    subprocess.check_call([sys.executable, '-m', 'pip', 'install', *missing_packages])
                    print(f'\nInstallation finished. [{checkmark}]')
                    time.sleep(2)
                    os.system('cls')
                else:
                    print(f'\nRequirements already installed. [{checkmark}]')
                    time.sleep(2)
                    os.system('cls')

            elif self.os_name == 'Linux':
                missing_packages = [pkg for pkg in packages if not self.is_package_installed(pkg)]

                if missing_packages:
                    print(f"Installing missing packages: {', '.join(missing_packages)}")
                    subprocess.check_call([sys.executable, '-m', 'pip', 'install', *missing_packages])
                    print(f'\nInstallation finished. [{checkmark}]')
                    time.sleep(2)
                    os.system('cls')
                else:
                    print(f'\nRequirements already installed. [{checkmark}]')
                    time.sleep(2)
                    os.system('clear')
            elif self.os_name == 'Linux' and os.geteuid() != 0:
                print("\nIt's recommended to run this script as root (sudo) "
                      "on Linux for system-wide installation.\n")
                print("You can run the script as root using: "
                      "sudo python pygeoseeker.py\n")
                print("If you want to install packages in a "
                      "virtual environment, use a virtual environment.\n")
                print("\nExiting...")
                sys.exit(1)
            else:
                missing_packages = [pkg for pkg in packages if not self.is_package_installed(pkg)]

                if missing_packages:
                    print(f"\nInstalling missing packages: {', '.join(missing_packages)}")
                    subprocess.check_call([sys.executable, '-m', 'pip', 'install', *missing_packages])
                    print(f'\nInstallation finished. [{checkmark}]')
                    time.sleep(2)
                    os.system('cls')
                else:
                    print(f'\nRequirements already installed. [{checkmark}]')
                    time.sleep(2)
                    sys.stdout.flush()
        except Exception as ex:
            print('\nAn exception occurred: \n', ex)
            sys.exit(1)

    @staticmethod
    def banner():
        from pyfiglet import Figlet
        from termcolor import colored

        f = Figlet(font='mini')

        print('\n')
        print(colored(f.renderText('P y G e o s e e k e r'),
                      'yellow',
                      attrs=['blink']))
        
    @classmethod
    def running_animation(cls):
        frames = ["|", "/", "-", "\\"]
        while True:
            for frame in frames:
                sys.stdout.write(f"\rRunning {frame}")
                sys.stdout.flush()
                time.sleep(0.1)  # Adjust the speed of animation here
    
    def os_hint(self):
        if self.os_name == 'Linux':
            print('Linux OS detected.')
            print('Hint: You must install the requirements '
                  'and run the script as root.\n')
        elif self.os_name == 'Windows':
            print('Windows OS detected.')
            print("Lock n' Load.\n")

    @staticmethod
    def action_menu():
        from colorama import Fore
        
        target_ip = input("\nSet the TARGET IP ADDRESS to track location: ")
        ip_input = str(target_ip)
        
        ipinfo_token = input("\nSet your IPinfo TOKEN: ")
        token_input = str(ipinfo_token)

        return ip_input, token_input
            
    # TODO: Linux execution script
    # TODO: Windows execution script
    def pygeoseeker(self):
        from colorama import Fore

        try:
            if self.os_name == 'Linux':
                handler = ipinfo.getHandler(self.ipinfo_token)
                details = handler.getDetails(self.target_ip)
                
                for key, value in details.all.items():
                    print(f"{key}: {value}")
                print('\n')
            else:
                handler = ipinfo.getHandler(self.ipinfo_token)
                details = handler.getDetails(self.target_ip)
                
                for key, value in details.all.items():
                    print(f"{key}: {value}")
                print('\n')
        except KeyboardInterrupt:
            print('\n')
            print(rf"{Fore.GREEN}PyGeoSeeker Terminated.{Fore.RESET}")
            print('\n')
            sys.exit(1)
    
    """MAIN RUNNER"""
    def main(self):
        self.banner()
        self.os_hint()
        self.target_ip, self.ipinfo_token = self.action_menu()
        self.ipinfo_token = self.action_menu()
        self.pygeoseeker()


if __name__ == '__main__':
    # You can run, but you can't hide
    PyGeoSeeker()
