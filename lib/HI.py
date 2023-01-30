from lib.Prv_dmas import *
class HI:
    def __init__(self, delimiter, primaryCode, otherDiagnosisCodes):
        self.delimiter = delimiter
        self.hi01_1 = 'ABK:'
        self.hi01_2 = primaryCode
        self.otherCodes = ['ABF:' + c for c in otherDiagnosisCodes]
        self.prv = Prv_dmas('PE', 'XXXXXXXXXX')
    
    def getSegment(self):
        histr = 
        if len(self.otherCodes) > 0:
            dataList = [self.hi01_1+self.hi01_2]
            dataList.extend(self.otherCodes)
            histr = ''.join(['HI*', '*'.join(dataList), '~'])
        else:   
            histr = ''.join(['HI*', self.hi01_1+self.hi01_2, '~'])
        
        return self.delimiter.join([histr, self.prv.getSegment()])