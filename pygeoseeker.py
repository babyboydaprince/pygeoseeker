import os
import sys
import subprocess
import time
import argparse
import ipinfo
import platform
from termcolor import cprint


class PyGeoSeeker:

    def __init__(self):
        self.os_name = platform.system()
        self.target_ip = ''
        self.access_token = ''
        self.main()

    @staticmethod
    def banner():
        from pyfiglet import Figlet
        f = Figlet(font='slant', width=50)
        cprint(f.renderText('P y G e o s e e k e r'), 'yellow', attrs=['blink', 'bold'])

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
                    os.system('clear')
                else:
                    print(f'\nRequirements already installed. [{checkmark}]')
                    time.sleep(2)
                    os.system('clear')

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

    def action_menu(self, ip_address, access_token, help_menu, os_detected):
        parser = argparse.ArgumentParser(description="Geolocation tracker")
        parser.add_argument(
            "--target",
            type=str,
            metavar="<target>",
            help="Target IP to track location",
        )
        parser.add_argument(
            "--access-token",
            type=str,
            metavar="<token>",
            help="IPinfo access token, to obtain one, sign up at https://ipinfo.io",
        )

        args = parser.parse_args()
        ip_address = args.target
        access_token = args.token
        help_menu = parser.print_help()

        if os_detected == 'Linux':
            try:
                if not ip_address and not access_token:
                    os.system('clear')
                    print('\n')
                    self.banner()
                    print('\n')
                    return help_menu
                elif not ip_address:
                    os.system('clear')
                    self.banner()
                    print('\n\nNo target specified, please provide a valid target.\n')
                    return False
                elif not access_token:
                    os.system('clear')
                    self.banner()
                    print('\n\nNo access token specified, please provide an access token.\n')
                    return False
                else:
                    return ip_address, access_token
            except KeyboardInterrupt:
                os.system('clear')
                self.banner()
                print('\n')
                cprint(f"PyGeoSeeker Terminated.", 'green')
                print('\n')
                return False

        elif os_detected == 'Windows':
            try:
                if not ip_address and not access_token:
                    os.system('cls')
                    print('\n')
                    self.banner()
                    print('\n')
                    return help_menu
                elif not ip_address:
                    os.system('cls')
                    self.banner()
                    print('\n\nNo target specified, please provide a valid target.\n')
                    return False
                elif not access_token:
                    os.system('cls')
                    self.banner()
                    print('\n\nNo access token specified, please provide an access token.\n')
                    return False
                else:
                    return ip_address, access_token
            except:
                os.system('cls')
                self.banner()
                print('\n')
                cprint(f"PyGeoSeeker Terminated.", 'green')
                print('\n')
                return False
        else:
            try:
                if not ip_address and not access_token:
                    print('\n')
                    self.banner()
                    print('\n')
                    return help_menu
                elif not ip_address:
                    print('\n')
                    self.banner()
                    print('\n\nNo target specified, please provide a valid target.\n')
                    return False
                elif not access_token:
                    print('\n')
                    self.banner()
                    print('\n\nNo access token specified, please provide an access token.\n')
                    return False
                else:
                    return ip_address, access_token
            except:
                print('\n')
                self.banner()
                print('\n')
                cprint(f"PyGeoSeeker Terminated.", 'green')
                print('\n')
                return False

    def pygeoseeker(target_ip, ipinfo_token):
        try:
            connection = ipinfo_token.getHandler(target_ip)
            get_details = connection.getDetails(target_ip)

            cprint(f"Geolocation Details for {target_ip}:", 'green', attrs=['bold'])
            cprint("--------------------------------------------------", 'green', attrs=['bold'])
            cprint("Key                 | Value", 'green', attrs=['bold'])
            cprint("--------------------------------------------------", 'green', attrs=['bold'])
            for key, value in get_details.all.items():
                cprint(f"{key:<20} | {value}", 'yellow')
            cprint("--------------------------------------------------", 'green', attrs=['bold'])
            print('\n')
        except KeyboardInterrupt:
            print('\n')
            cprint(f"PyGeoSeeker Terminated.", 'green')
            print('\n')
        except Exception as e:
            cprint(f"Error: {e}", 'red')

    def main(self):
        required_packages = [
            'ipinfo',
            'termcolor',
            'colorama',
            'pyfiglet'
        ]

        if sys.argv[1] == '--target' and sys.argv[2] == '--access-token':
            self.install_missing_packages(required_packages)
            self.target_ip, self.ipinfo_token = self.action_menu('--target', '--access-token', [], self.os_name)
            if self.target_ip and self.ipinfo_token:
                self.pygeoseeker(self.target_ip, self.ipinfo_token)

        elif sys.argv[1] == '--help':
            print('\n')
            self.banner()
            self.target_ip, self.ipinfo_token = self.action_menu([], [], '--help', self.os_name)
            print('\n')
                
        else:
            print('\n')
            self.banner()


if __name__ == '__main__':
    # You can run, but you can't hide
    PyGeoSeeker()
