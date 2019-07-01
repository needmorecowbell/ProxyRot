from proxyrot import ProxyRot

torpass=""
pr = ProxyRot(password=torpass)


print("Original IP: "+ pr.get_ip())
for x in range(0,5):
    print("IP: "+pr.get_tor_ip())
    pr.reset_tor_identity()
