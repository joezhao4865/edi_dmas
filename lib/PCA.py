from lib.Reference import *
from lib.Constants import *
from lib.Taxonomy import *
class PCA:
    def __init__(self, dilimiter, tax):
        self.CONSTANT = Constant()
        self.dilimiter = dilimiter
        self.nm101 = '82'
        self.nm102 = '2'
        self.org_name = self.CONSTANT.PROVIDER_ENTITY_NAME
        self.nm104 = ''
        self.nm105 = ''
        self.nm106 = ''
        self.nm107 = ''
        self.nm108 = 'XX'
        self.nm109 = self.CONSTANT.NPI
        self.taxonomy = tax
        
        
    def getSegment(self):
        return self.dilimiter.join([
                '*'.join(['NM1', self.nm101, self.nm102, self.org_name, self.nm104, self.nm105, self.nm106, self.nm107, self.nm108, self.nm109+'~' ]),                
                self.taxonomy
                
            ])