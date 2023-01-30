from lib.Constants import *
class RenderingProvider:  
    def __init__(self, required = False, pcaFirstName = '', pcaLastName = ''):
        self.CONSTANT = Constant()
        self.required = required
        self.providerCode = '82'
        self.qualifier = '1' # person
        self.lastName = pcaFirstName
        self.firstName = pcaLastName
        self.nm105 = ''
        self.nm106 = ''
        self.nm107 = ''
        self.IDQualifier = 'XX' # for NPI
        self.NPI = self.CONSTANT.NPI
    
    def getSegment(self):
        return ('', ''.join(['NM1*', '*'.join([self.providerCode, self.qualifier, self.lastName, self.firstName, self.nm105, self.nm106, self.nm107, self.IDQualifier, self.NPI]), '~']))[self.required]
    
    def required(self):
        return self.required