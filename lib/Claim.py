from lib.Constants import *
from lib.Reference import *
from lib.Clients import *
class Claim:
    def __init__(self, delimiter, claimID, billedAmt, freqCode, serviceZip = '22066', sigCode = ''):
        self.delimiter = delimiter
        self.claimId = claimID
        self.billedAmt = '{:.2f}'.format(billedAmt)
        self.clm03 = ''
        self.clm04 = ''
        self.facilityCode = ('12', '11')[serviceZip == Constant().PROVIDER_SHORT_ZIP]
        self.facilityQualifier = 'B'
        self.freqCode = freqCode
        self.sigOnFile = 'Y'
        self.acceptCode = 'A'
        self.beneIdAssigned = 'Y'
        self.beneInfoRelease = 'Y'
        self.sigCode = sigCode
        self.Reference = Reference(True, 'EA', 'AuthorizationInClaim')
    
    def getSegment(self):
        claimInfo = (''.join(['CLM*', '*'.join([self.claimId, self.billedAmt, self.clm03, self.clm04, ':'.join([self.facilityCode, self.facilityQualifier, self.freqCode]), self.sigOnFile, self.acceptCode, self.beneIdAssigned, self.beneInfoRelease, self.sigCode]), '~']), ''.join(['CLM*', '*'.join([self.claimId, self.billedAmt, self.clm03, self.clm04, ':'.join([self.facilityCode, self.facilityQualifier, self.freqCode]), self.sigOnFile, self.acceptCode, self.beneIdAssigned, self.beneInfoRelease]), '~']))[self.sigCode == '']
        
        return self.delimiter.join(claimInfo, self.Reference.getSegment())