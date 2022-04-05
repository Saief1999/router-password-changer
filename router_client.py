from base64 import b64encode
import requests
from operations import Operations

class RouterClient:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0"})
        self.host = "http://192.168.1.1"
        self.op = Operations()


    def routerGetRequest(self, cmd:str):
        """
        General purpose get request
        """
        response = self.session.get(f"{self.host}/reqproc/proc_get", params={"cmd": cmd, "isTest": "false"})
        return response.json()

    def routerPostRequest(self, form:str, data:dict={}):
        """
        General purpose post request
        """
        data["isTest"] = "false"
        data["goformId"] = form
        response = self.session.post(f"{self.host}/reqproc/proc_post", data=data)
        return response.json()

    def getRandomLoginCode(self)->str:
        """
        Gets a random login code from the server
        """
        response = self.routerPostRequest("GET_RANDOM_LOGIN")
        return response["random_login"]

    def login(self, username:str, password:str):
        """
        Login to Admin account
        """
        random_login = self.getRandomLoginCode()

        login_response = self.routerPostRequest(
            "LOGIN",
            { 
                "username": self.op.b64encode(username),
                "password": self.op.b64encode(self.op.sha256(random_login + password)),
            })

        cookie = login_response["cookie"]
        return self.op.sha256(cookie)

    def get_token(self):
        """
        Get CSRF token from router
        """

        response = self.routerGetRequest("get_token")
        return response["token"]

    
    def set_wifi_settings(self, username:str, password:str, ssid:str, passphrase:str,
     broadcastSsidEnabled=0, MAX_Access_num=0, security_mode="WPA2PSK",
     cipher=1, show_qrcode_flag=0, wep_default_key=0, wep_key_1=12345,
     WEP1Select=0, pmf_status=1, security_shared_mode=1
     ):
        """
        Sets the wifi settings
        Returns True if the setttings have been changed succesfully
        """

        hashed_cookie = self.login(username, password)
        self.session.headers.update({"Cookie": f"random={hashed_cookie}" }) # will be available for future requests
        csrf_token = self.op.sha256(self.get_token())

        response = self.routerPostRequest(
            "SET_WIFI_SSID1_SETTINGS",
            {
                "ssid": ssid,
                "passphrase": self.op.b64encode(passphrase),
                "CSRFToken": csrf_token,

                # These can be configured if needed
                "broadcastSsidEnabled": broadcastSsidEnabled,
                "MAX_Access_num": MAX_Access_num,
                "security_mode": security_mode,
                "cipher": cipher,
                "show_qrcode_flag": show_qrcode_flag,
                "wep_default_key": wep_default_key,
                "wep_key_1": wep_key_1,
                "WEP1Select": WEP1Select,
                "pmf_status": pmf_status,
                "security_shared_mode": security_shared_mode
            }
        )


        result = response["result"]

        return result == "success"

