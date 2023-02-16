class ServiceLine:
    def __init__(self, dilimiter, serviceLineHeader, serviceDate, claimReference, tax, contract = ''):
        self.dilimiter = dilimiter
        self.lineHeader = serviceLineHeader
        self.serviceDate = serviceDate
        self.contract = contract
        self.reference = claimReference
        self.taxonomy = tax
        
    def getSegment(self):
        return (self.dilimiter.join([self.lineHeader, self.serviceDate, self.contract, self.reference, self.taxonomy]), self.dilimiter.join([self.lineHeader, self.serviceDate, self.reference, self.taxonomy]))[self.contract == '']