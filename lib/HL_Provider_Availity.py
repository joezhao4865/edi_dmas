class HL_Provider_Availity:
    def __init__(self, hlChild = True, hlIndex = 1, hlInfoSource = '20'):
        self.hlIndex = str(hlIndex)
        self.hl02 = ''
        self.infoSource = hlInfoSource
        self.hlChild = ('', '1')[hlChild]
    
    def getSegment(self):
        return ''.join(['HL*', '*'.join([self.hlIndex, self.hl02, self.infoSource, self.hlChild]),  '~'])