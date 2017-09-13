class zone:
    zonefiledict = {"Domain" : '' , "TTL" : '' , "records" : {"SOA" : {} "A" : {} , "AAAA" : {} , "NS" : {} , "MX" : {} , "CNAME" : {} ,  "DNAME"  : {} , "TXT" : {} }}
    TTL          = ""
    SOArecords   = []
    Arecords     = []
    AAAArecords  = []
    NSrecords    = []
    MXrecords    = []
    CNAMErecords = []
    DNAMErecords = []
    PTRrecords   = []
    TXTrecords   = []

    def getAll(self):
        return self.SOArecords + self.Arecords + self.AAAArecords + self.NSrecords + self.MXrecords + self.CNAMErecords + self.DNAMErecords + self.PTRrecords + self.TXTrecords
    def getSOA(self):
        return self.zonefiledict["records"]["SOA"]
    def getA(self):
        return self.zonefiledict["records"]["A"]
    def getAAAA(self):
        return self.zonefiledict["records"]["AAAA"]
    def getNS(self):
        return self.zonefiledict["records"]["NS"]
    def getMX(self):
        return self.zonefiledict["records"]["MX"]
    def getCNAME(self):
        return self.zonefiledict["records"]["CNAME"]
    def getDNAME(self):
        return self.zonefiledict["records"]["DNAME"]
    def getPTR(self):
        return self.zonefiledict["records"]["PTR"]
    def getTXT(self):
        return self.zonefiledict["records"]["TXT"]
    def setSOA(self,SOArecord):
        return self.SOArecords.append(SOArecord)
    def addA(self,Arecord):
        return self.Arecords.append(Arecord)
    def addAAAA(self,AAAArecord):
        return self.AAAArecords.append(AAAArecord)
    def addNS(self,NSrecord):
        return self.NSrecords.append(NSrecord)
    def addMX(self,MXrecord):
        return self.MXrecords.append(MXrecord)
    def addCNAME(self,CNAMErecord):
        return self.CNAMErecords.append(CNAMErecord)
    def addDNAME(self,DNAMErecord):
        return self.DNAMErecords.append(DNAMErecord)
    def addPTR(self,PTRrecord):
        return self.PTRrecords.append(PTRrecord)
    def addTXT(self,TXTrecord):
        return self.TXTrecords.append(TXTrecord)

class records:
    request = ""
    awnser  = ""
    def __init__(self, request,awnser):
        self.request = request
        self.awnser  = awnser
        print(awnser)
    def getAwnser(self):
        return self.awnser
    def getRequest(self):
        return self.awnser
    def setAwnser(self, awnser):
        self.awnser = awnser
    def setRequest(self, request):
        self.request = request

class SOA():
    def __init__(self, request,awnser):
        records.__init__(self,request,awnser)


class A(records):
    def __init__(self, request,awnser):
        records.__init__(self,request,awnser)


class AAAA(records):
    def __init__(self, request,awnser):
        records.__init__(self,request,awnser)

class NS(records):
    def __init__(self, request,awnser):
        records.__init__(self,request,awnser)


class MX(records):
    def __init__(self, request,awnser):
        records.__init__(self,request,awnser)


class CNAME(records):
    def __init__(self, request,awnser):
        records.__init__(self,request,awnser)


class DNAME(records):
    def __init__(self, request,awnser):
        records.__init__(self,request,awnser)


class PTR(records):
    def __init__(self, request,awnser):
        records.__init__(self,request,awnser)


class TXT(records):
    def __init__(self, request,awnser):
        records.__init__(self,request,awnser)
