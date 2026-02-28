import re
import sys


def main():
    address = input("IPv4 Address: ")
    val = validate(address)
    print(val)



def validate(ip):
    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$",ip):
        l_nb = ip.split(".")
        for nb in l_nb:
            if len(nb)>1 and nb[0]=="0":
                return False
            if int(nb)<0 or int(nb)>255:
                return False
        return True
    else:
        return False



if __name__ == "__main__":
    main()
