class HI:
    def __init__(self, primaryCode, otherDiagnosisCodes):
        self.hi01_1 = 'ABK:'
        self.hi01_2 = primaryCode
        self.otherCodes = ['ABF:' + c for c in otherDiagnosisCodes]
        
    
    def getSegment(self):
        
        if len(self.otherCodes) > 0:
            dataList = [self.hi01_1+self.hi01_2]
            dataList.extend(self.otherCodes)
            return ''.join(['HI*', '*'.join(dataList), '~'])
        else:   
            return ''.join(['HI*', self.hi01_1+self.hi01_2, '~'])