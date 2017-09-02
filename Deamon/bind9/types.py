class zone:
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
        return self.SOArecords
    def getA(self):
        return self.Arecords
    def getAAAA(self):
        return self.AAAArecords
    def getNS(self):
        return self.NSrecords
    def getMX(self):
        return self.MX
    def getCNAME(self):
        return self.CNAMErecords
    def getDNAME(self):
        return self.DNAMErecords
    def getPTR(self):
        return self.PTRrecords
    def getTXT(self):
        return self.TXTrecords

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
