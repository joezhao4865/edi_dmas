class ServiceLine:
    def __init__(self, dilimiter, serviceLineHeader, serviceDate, claimReference, pca, spca, pickup, contract = ''):
        self.dilimiter = dilimiter
        self.lineHeader = serviceLineHeader
        self.serviceDate = serviceDate
        self.contract = contract
        self.reference = claimReference
        self.pca = pca
        self.spca = spca
        self.pickup = pickup
        
    def getSegment(self):
        return (
            self.dilimiter.join([self.lineHeader, self.serviceDate, self.contract, self.reference, self.pca, self.spca, self.pickup]), 
            self.dilimiter.join([self.lineHeader, self.serviceDate, self.reference, self.pca, self.spca, self.pickup])
        )[self.contract == '']