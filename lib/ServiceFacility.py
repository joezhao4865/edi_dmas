from lib.Constants import *
class ServiceFacility:  
    def __init__(self, required = False, facilityAddress = None):
        self.CONSTANT = Constant()
        self.required = required
        self.providerCode = '77'
        self.qualifier = '2' # org
        self.name = self.CONSTANT.PROVIDER_ENTITY_NAME
        self.nm104 = ''
        self.nm105 = ''
        self.nm106 = ''
        self.nm107 = ''
        self.IDQualifier = 'XX' # for NPI
        self.NPI = self.CONSTANT.NPI
        self.address = facilityAddress
    
    def getSegment(self):
        return ('', ''.join(['NM1*', '*'.join([self.providerCode, self.qualifier, self.name, self.nm104, self.nm105, self.nm106, self.nm107, self.IDQualifier, self.NPI]), '~', '' if self.address == None else self.address.getSegment() ]))[self.required]
    
    def required(self):
        return self.required