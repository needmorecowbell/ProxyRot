import requests
from torrequest import TorRequest
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class ProxyRot():
    """docstring for ProxyRot."""
    tr = None
    url= None
    password = ""
    proxies = []
    chromedriver="/usr/local/bin/chromedriver"

    def __init__(self, password= None, url= None):
        self.password= password

        if(password is not None):
            self.tr = TorRequest(password=self.password)
        else:
            self.tr = TorRequest()

        self.url = url

        self.options = Options()
        self.options.add_argument('--headless')
        self.options.add_argument('--disable-gpu')  # Last I checked this was necessary

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

    def scrape_proxies_country(self):
        countries=["Russia","China", "India", "Ukraine",
        "Indonesia","Brazil", "Canada","Pakistan", "United Kingdom","Iran",
        "Thailand"]
        countries=["Russia","China"]
        url = "http://www.gatherproxy.com/proxylist/country/?c="
        proxies={}
   
        driver = webdriver.Chrome(self.chromedriver, options=self.options)

        try:
            for country in countries:
                driver.get(url+country)
                time.sleep(2)
                #print(driver.page_source)
                page_content = BeautifulSoup(''.join(driver.page_source), "html.parser")
                    
                proxy_table = page_content.find("div", attrs={"class": "proxy-list"})
                proxies_pre = proxy_table.findAll("tr")
                proxies[country]=[]
                
                for proxy in proxies_pre:
                    proxies[country].append(proxy.attrs)

            return proxies
        except Exception as e:
            print(e)
            return None

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
