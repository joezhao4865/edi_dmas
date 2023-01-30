class Subscriber:
    def __init__(self, sbrHeader, sbrName, sbrAddress, sbrDmg, dilimiter): 
        self.dilimiter = dilimiter
        self.sbrHeader = sbrHeader
        self.nameInfo = sbrName
        self.address = sbrAddress
        self.dmg = sbrDmg
        
    def getSegment(self):
        return self.dilimiter.join([self.sbrHeader, self.nameInfo, self.address, self.dmg])