from lib.Constants import *
from lib.Reference import *

class RenderingProvider:  
    def __init__(self, required, dilimiter, tax, pcaFirstName = '', pcaLastName = ''):
        self.dilimiter = dilimiter
        self.CONSTANT = Constant()
        self.required = required
        self.providerCode = '82'
        self.qualifier = '2' # person
        self.lastName = self.CONSTANT.PROVIDER_ENTITY_NAME
        self.firstName = ''
        self.nm105 = ''
        self.nm106 = ''
        self.nm107 = ''
        self.IDQualifier = 'XX' # for NPI
        self.NPI = self.CONSTANT.NPI
        self.renderingPrTax = ('', tax)[required]
        #self.ref = Reference(True, 'EI', self.CONSTANT.EIN).getSegment()
        
    def getSegment(self):
        return (
                '', 
                self.dilimiter.join([
                    '*'.join(['NM1', self.providerCode, self.qualifier, self.lastName, self.firstName, self.nm105, self.nm106, self.nm107, self.IDQualifier, self.NPI+'~']),
                    self.renderingPrTax
                ])
        )[self.required]
    
    def required(self):
        return self.required