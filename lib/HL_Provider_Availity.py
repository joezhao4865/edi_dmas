from lib.Taxonomy import *
class HL_Provider_Availity:
    def __init__(self, dilimiter, proc, hlChild = True, needTax = False, hlIndex = 1, hlInfoSource = '20'):
        self.dilimiter = dilimiter
        self.hlIndex = str(hlIndex)
        self.hl02 = ''
        self.infoSource = hlInfoSource
        self.hlChild = ('', '1')[hlChild]
        self.billerTax = ('', Taxonomy('BI', proc).getSegment())[needTax]
    def getSegment(self):
        return self.dilimiter.join([ 
                '*'.join(['HL', self.hlIndex, self.hl02, self.infoSource, self.hlChild+'~']),
                self.billerTax
            ])