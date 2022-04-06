
import subprocess

class WifiManager:

    def get_current_wifi_ssid(self)->str:
        """
        Get the current wifi ssid
        """
        
        output = subprocess.check_output(["nmcli", "connection", "show", "--active"])
        decoded_output = output.decode("utf-8")
        return decoded_output.splitlines()[1].split(' ')[0]

    
    def print_current_wifi(self)->None:
        """
        Prints informations about the current wifi
        """
        subprocess.run(["nmcli", "device", "wifi", "show-password"])

    def change_wifi_password(self, ssid:str, password:str)->None:
        """
        Change the the current wifi password of a certain ssid
        """
        subprocess.run(["nmcli", "connection", "modify", "id", ssid, "wifi-sec.psk", password])