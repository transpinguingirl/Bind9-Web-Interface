import types
def loadzone(file):
    with open(file) as zonefile:
        zonefile = types.zone()
        for line in zonefile:
            if "$TTL " in line:
                TTL = line.split(" ")[1]
            else if "SOA" in line:
                print("SOA")
            else if " NS " in line:
                zonefile.addNS(*record(line))
                print("NS")
            else if " A " in line:
                zonefile.addA(*record(line))
                print("A")
            else if " MX " in line:
                zonefile.addMX(*record(line))
                print("MX")
            else if " AAAA " in line:
                zonefile.addAAAA(*record(line))
                print("AAAA")
            else if " CNAME " in line:
                zonefile.addCNAME(*record(line))
                print("CNEM")
            else if " DNAME " in line:
                zonefile.addDNAME(*record(line))
                print("DNAME")
            else if " TXT " in line:
                zonefile.addTXT(*record(line))
                print("TXT")
            else if " IN " in line:
                print("IN")
        return(zonefile)
def record(data):
    data = data.split(" IN ")
    data[0] = data[0].replace(" ","")
    data[1] = data[1].replace(" ","")
    return(data[0],data[1])
