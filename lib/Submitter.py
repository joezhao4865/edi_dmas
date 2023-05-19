from lib.Constants import *
class Submitter:
    def __init__(self):
        self.CONSTANT = Constant()
        self.nm01 = '41' # code for submitter
        self.nm02 = '2'  # entity not person which is 1
        self.nm03 = self.CONSTANT.PROVIDER_ENTITY_NAME
        self.nm04 = ''
        self.nm05 = ''
        self.nm06 = ''
        self.nm07 = ''
        self.nm08 = '46' # ETIN not SSN
        self.nm09 = self.CONSTANT.SENDERID  # Can EIN be ETIN for availity, or it needs to be sender id?
        
        
    def getSegment(self):
        return ''.join(['NM1*', '*'.join([self.nm01, self.nm02, self.nm03, self.nm04, self.nm05, self.nm06, self.nm07, self.nm08, self.nm09]),  '~'])    