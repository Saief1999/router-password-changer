import argparse
import secrets
import string
from router_client import RouterClient
from wifi_manager import WifiManager
import logging

class PasswordChanger:
    """
    Changes password on router
    """
    def __init__(self, login, password, passphrase) -> None:
        self.wifi_manager = WifiManager()
        self.login = login
        self.password = password
        self.ssid = self.wifi_manager.get_current_wifi_ssid()
        self.passphrase = passphrase
        self.router_client = RouterClient()
    
    def change_password(self) -> None:
        """
        Change password on router
        """
        logging.info(f"Changing password of {self.ssid}")
        result = self.router_client.set_wifi_settings(self.login,self.password, self.ssid, self.passphrase)
        if (result):
            logging.info("Password changed successfully!")
            logging.info("Changing current password...")
            self.wifi_manager.change_wifi_password(self.ssid, self.passphrase)
        else:
            logging.error("Error while changing password!")

if __name__ == "__main__":
    parser = parser = argparse.ArgumentParser(description='Change router password.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-pp", "--passphrase", help="Wifi passphrase", default=''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(20)))
    parser.add_argument("-a", "--admin", help="Admin account login.", default="admin")
    parser.add_argument("-p","--password", help="Admin account password.", default="admin")
    args = parser.parse_args()

    password_changer = PasswordChanger(args.admin,args.password, args.passphrase)
    password_changer.change_password()
    password_changer.wifi_manager.print_current_wifi()
