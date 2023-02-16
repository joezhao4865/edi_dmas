class HL_Provider_Availity:
    def __init__(self, dilimiter, tax, hlChild = True, hlIndex = 1, hlInfoSource = '20'):
        self.dilimiter = dilimiter
        self.hlIndex = str(hlIndex)
        self.hl02 = ''
        self.infoSource = hlInfoSource
        self.hlChild = ('', '1')[hlChild]
        self.prv = tax.getSegment()
    
    def getSegment(self):
        return self.dilimiter.join([''.join(['*'.join(['HL', self.hlIndex, self.hl02, self.infoSource, self.hlChild]), '~']), self.prv])