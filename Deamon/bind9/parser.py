from . import types
def loadzone(file):
    with open(file) as zonefileraw:
        zonefile = types.zone()
        for line in zonefileraw:
            if "$TTL " in line:
                TTL = line.split(" ")[1]
            elif "SOA" in line:
                print("SOA")
            elif " NS " in line:
                print(len(record(line)))
                zonefile.addNS(record(line))
                print("NS")
            elif " A " in line:
                zonefile.addA(*record(line))
                print("A")
            elif " MX " in line:
                zonefile.addMX(*record(line))
                print("MX")
            elif " AAAA " in line:
                zonefile.addAAAA(*record(line))
                print("AAAA")
            elif " CNAME " in line:
                zonefile.addCNAME(*record(line))
                print("CNEM")
            elif " DNAME " in line:
                zonefile.addDNAME(*record(line))
                print("DNAME")
            elif " TXT " in line:
                zonefile.addTXT(*record(line))
                print("TXT")
            elif " IN " in line:
                print("IN")
        return(zonefile)
def record(data):
    print(data)
    data = data.split(" IN ")
    print(data)
    data[0] = data[0].replace(" ","")
    data[1] = data[1].replace(" ","")
    print(data)
    return(data[0],data[1])
