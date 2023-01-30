class ServiceLine:
    def __init__(self, dilimiter, serviceLineHeader, serviceDate, claimReference, contract = ''):
        self.dilimiter = dilimiter
        self.lineHeader = serviceLineHeader
        self.serviceDate = serviceDate
        self.contract = contract
        self.reference = claimReference
        
    def getSegment(self):
        return (self.dilimiter.join([self.lineHeader, self.serviceDate, self.contract, self.reference]), self.dilimiter.join([self.lineHeader, self.serviceDate, self.reference]))[self.contract == '']