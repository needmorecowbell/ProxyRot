from proxyrot import ProxyRot
import argparse

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
