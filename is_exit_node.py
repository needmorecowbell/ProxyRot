import requests
import argparse

iplist= []
def get_exit_nodes():
    content = requests.get("https://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=1.1.1.1").text

    for line in content.split("\n"):
        if("#" not in line):
            iplist.append(line)

def is_exit_node(ip):
    return ip in iplist


parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
parser.add_argument("ip", help="ip to check")

args = parser.parse_args()

if(args.verbose):
    print("Checking ip: "+args.ip)

get_exit_nodes()
print(is_exit_node(args.ip))
