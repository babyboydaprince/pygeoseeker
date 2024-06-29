import os
import platform
import subprocess
import sys
import time
import ipinfo
from termcolor import cprint
from argparse import ArgumentParser


class PyGeoSeeker:

    def __init__(self):
        self.os_name = platform.system()
        self.main()

    @staticmethod
    def banner():
        from pyfiglet import Figlet
        f = Figlet(font='slant')
        print('\n')
        cprint(f.renderText('P y G e o'), 'yellow')
        cprint(f.renderText('S e e k e r'), 'yellow')
        print('\n')

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

    def main(self):
        parser = ArgumentParser(description='--------Geolocation tracker--------',
                                usage='python pygeoseeker.py --help',
                                epilog='python3 pygeoseeker.py '
                                       '--target [IP] '
                                       '--access-token [TOKEN]')

        parser.add_argument_group('Required Arguments:')

        parser.add_argument(
            "-t", "--target",
            type=str,
            metavar="<target>",
            help="Target IP to track location",
            required=True
        )
        parser.add_argument(
            "-token", "--access-token",
            type=str,
            metavar="<token>",
            help="IPinfo access token, to obtain one, sign up at https://ipinfo.io",
            required=True
        )

        args = parser.parse_args()

        self.pygeoseeker(args.target, args.access_token)

    @staticmethod
    def pygeoseeker(target_ip, ipinfo_token):
        try:
            connection = ipinfo.getHandler(ipinfo_token)
            get_details = connection.getDetails(target_ip)
            # PyGeoSeeker.banner()
            cprint(f"Geolocation Details for {target_ip}:", 'green', attrs=['bold'])
            cprint("--------------------------------------------------", 'green', attrs=['bold'])
            cprint("Key                  | Value", 'green', attrs=['bold'])
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


if __name__ == '__main__':
    # You can run, but you can't hide
    required_packages = [
        'ipinfo',
        'termcolor',
        'colorama',
        'pyfiglet'
    ]

    PyGeoSeeker.banner()
    PyGeoSeeker().install_missing_packages(required_packages)
    PyGeoSeeker.banner()
    PyGeoSeeker()
