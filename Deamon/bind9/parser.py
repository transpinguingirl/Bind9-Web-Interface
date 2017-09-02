def loadzone(file):
    with open(file) as zonefile:
        for line in zonefile:
            if "$TTL" in line:
                TTL = line.split(" ")[1]
            else if ""
            
