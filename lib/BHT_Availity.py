class BHT_Availity:
    def __init__(self, stCounter, creationDate, creationTime):
        self.bht01 = '0019'
        self.bht02 = '00'
        self.bht03 = stCounter
        self.bht04 = creationDate
        self.bht05 = creationTime
        self.bht06 = 'CH'
    
    def getSegment(self):
        return ''.join(['BHT*', '*'.join([self.bht01, self.bht02, self.bht03, self.bht04, self.bht05, self.bht06]), '~'])