import requests
from torrequest import TorRequest
import argparse


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
            reponse = self.tr.get('http://ipinfo.io/ip')
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

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    parser.add_argument("-t", "--tor", help="tor mode", action="store_true")

    parser.add_argument("-p", "--pswd", dest="pswd",
                    help="password for tor server")


    parser.add_argument("url", help="url to grab")

    args = parser.parse_args()

    if(args.tor):
        if(args.verbose):
            print("Using tor for request")

        if(args.pswd):
            if(args.verbose):
                print("Setting password for tor server")

            pr = ProxyRot(password=args.pswd)
        else:
            pr= ProxyRot()

        response = pr.get(args.url)

        if(response is not None):
            print(response.content)




if __name__ == "__main__":
    main()
