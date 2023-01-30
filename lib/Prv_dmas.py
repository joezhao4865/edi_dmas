class Prv_dmas:
    def __init__(self, segID, taxCode='XXXXXXXXXX'):
        self.segID = segID
        self.prv02 = 'PXC'
        self.claimTaxonomy = taxCode
    
    def getSegment(self):
        return ''.join(['*'.join(['PRV', self.segID, self.prv02, self.claimTaxonomy]), '~'])