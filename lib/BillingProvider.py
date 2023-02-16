from lib.Constants import *
from lib.Prv_dmas import *
class BillingProvider:
    def __init__(self, dilimiter):
        self.CONSTANT = Constant()
        self.dilimiter = dilimiter
        
    def getSegment(self):
        return self.dilimiter.join([''.join(['NM1*', '*'.join(['85', '2', self.CONSTANT.PROVIDER_ENTITY_NAME, '', '', '', '', 'XX', self.CONSTANT.NPI]),  '~']), ''.join(['N3*', self.CONSTANT.PROVIDER_ADDRESS1+' '+self.CONSTANT.PROVIDER_ADDRESS2, '~']), ''.join(['N4*', '*'.join([self.CONSTANT.PROVIDER_CITY, self.CONSTANT.PROVIDER_STATE, self.CONSTANT.PROVIDER_ZIP]), '~']), ''.join(['REF*', 'EI*', self.CONSTANT.EIN, '~'])])