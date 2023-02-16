from lib.Constants import *
class RenderingProvider:  
    def __init__(self, delimiter, tax, required = False,  pcaFirstName = '', pcaLastName = ''):
        self.CONSTANT = Constant()
        self.delimiter = delimiter
        self.prv = tax.getSegment()
        self.required = required
        self.providerCode = '82'
        self.qualifier = '1' # person
        self.lastName = self.CONSTANT.PROVIDER_ENTITY_NAME
        self.firstName = ''
        self.nm105 = ''
        self.nm106 = ''
        self.nm107 = ''
        self.IDQualifier = 'XX' # for NPI
        self.NPI = self.CONSTANT.NPI
    
    def getSegment(self):
        return ('', self.delimiter.join([self.prv, ''.join(['*'.join(['NM1', self.providerCode, self.qualifier, self.lastName, self.firstName, self.nm105, self.nm106, self.nm107, self.IDQualifier, self.NPI]), '~'])]))[self.required]
    
    def required(self):
        return self.required