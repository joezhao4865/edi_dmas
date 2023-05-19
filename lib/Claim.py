from lib.Constants import *
class Claim:
    def __init__(self, claimID, billedAmt, freqCode, serviceZip = '22066', sigCode = ''):
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
    
    def getSegment(self):
        return (''.join(['CLM*', '*'.join([self.claimId, self.billedAmt, self.clm03, self.clm04, ':'.join([self.facilityCode, self.facilityQualifier, self.freqCode]), self.sigOnFile, self.acceptCode, self.beneIdAssigned, self.beneInfoRelease, self.sigCode]), '~']), ''.join(['CLM*', '*'.join([self.claimId, self.billedAmt, self.clm03, self.clm04, ':'.join([self.facilityCode, self.facilityQualifier, self.freqCode]), self.sigOnFile, self.acceptCode, self.beneIdAssigned, self.beneInfoRelease]), '~']))[self.sigCode == '']