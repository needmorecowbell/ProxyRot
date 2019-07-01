from proxyrot import ProxyRot

pr = ProxyRot(password="trexxoASD")

for x in range(0,5):
    print("IP: "+pr.get("http://ipinfo.io/ip").text)
    pr.reset_tor_identity()
