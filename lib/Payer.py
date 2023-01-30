class Payer:
    def __init__(self, dilimiter, orgName, payerId, payerAddress = ''):
        self.dilimiter = dilimiter
        self.nm101 = 'PR'
        self.nm102 = '2'
        self.nm103 = orgName
        self.nm104 = ''
        self.nm105 = ''
        self.nm106 = ''
        self.nm107 = ''
        self.nm108 = 'PI'
        self.nm109 = payerId
        self.address = payerAddress
        
    def getSegment(self):
        return (self.dilimiter.join([''.join(['NM1*', '*'.join([self.nm101, self.nm102, self.nm103, self.nm104, self.nm105, self.nm106, self.nm107, self.nm108, self.nm109]), '~']), self.address]), self.dilimiter.join([''.join(['NM1*', '*'.join([self.nm101, self.nm102, self.nm103, self.nm104, self.nm105, self.nm106, self.nm107, self.nm108, self.nm109]), '~'])]))[self.address == '']