import requests
from torrequest import TorRequest


class ProxyRot():
    """docstring for ProxyRot."""
    tr = None
    url= None
    password = ""
    proxies = []

    def __init__(self, password= None, url= None):
        self.password= password

        if(password is not None):
            self.tr = TorRequest(password=self.password)
        else:
            self.tr = TorRequest()

        self.url = url

    def get_ip(self):
        try:
            response= requests.get('http://ipinfo.io/ip')
        except Exception as e:
            print(str(e))
            return None

        return response.text

    def reset_tor_identity(self):
        self.tr.reset_identity()
        self.tr = TorRequest(password=self.password)

    def get_tor_ip(self):
        try:
            response = self.tr.get('http://ipinfo.io/ip')
        except Exception as e:
            print(str(e))
            return None
        return response.text

    def get(self, url):
        try:
            response = self.tr.get(url)
        except Exception as e:
            print(str(e))
            return None
        return response
