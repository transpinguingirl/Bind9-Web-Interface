def loadzone(file):
    with open(file) as zonefile:
        for line in zonefile:
            if "$TTL " in line:
                TTL = line.split(" ")[1]
            else if "SOA" in line:
                print("SOA")
            else if " NS " in line:
                print("NS")
            else if " A " in line:
                print("A")
            else if " MX " in line:
                print("MX")
            else if " AAAA " in line:
                print("AAAA")
            else if " CNAME " in line:
                print("CNEM")
            else if " DNAME " in line:
                print("DNAME")
            else if " TXT " in line:
                print("TXT")
            else if " IN " in line:
                print("IN")
def record(data):
    data = data.split(" IN ")
    data[0] = data[0].replace(" ","")
    data[1] = data[1].replace(" ","")
    return(data[0],data[1])
