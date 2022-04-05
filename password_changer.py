import argparse
import secrets
import string
from router_client import RouterClient

class PasswordChanger:
    """
    Changes password on router
    """
    def __init__(self, login, password, ssid, passphrase) -> None:
        self.login = login
        self.password = password
        self.ssid = ssid
        self.passphrase = passphrase
        self.router_client = RouterClient()
    
    def change_password(self) -> None:
        """
        Change password on router
        """
        result = self.router_client.set_wifi_settings(self.login,self.password, self.ssid, self.passphrase)
        if (result):
            print("Password changed successfully!")
        else:
            print("Error while changing password!")

if __name__ == "__main__":
    parser =     parser = argparse.ArgumentParser(description='Change router password.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("ssid", help="Wifi name.")
    parser.add_argument("-pp", "--passphrase", help="Wifi passphrase", default=''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(20)))
    parser.add_argument("-a", "--admin", help="Admin account login.", default="admin")
    parser.add_argument("-p","--password", help="Admin account password.", default="admin")
    args = parser.parse_args()

    password_changer = PasswordChanger(args.admin,args.password, args.ssid, args.passphrase)
    password_changer.change_password()