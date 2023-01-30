class ST_Availity:
    def __init__(self, stControlNumber, stIndex):
        self.st01 = '837'
        self.st02 = stControlNumber
        self.st03 = '005010X222A1'
        self.index = stIndex
    
    def getSegment(self):
        return ''.join(['ST*', '*'.join([self.st01, self.st02, self.st03]),  '~'])
        
    def getSTIndex(self):
        return self.index