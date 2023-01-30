class IEA_Availity:
    #params:
    #functional group count: string length 1 - GS/GE count in the file max value 10000
    #control number: string length 9 - sender assigned unique control number
    def __init__(self, fgcount, controlNumber):
        self.count = fgcount
        self.controlNumber = controlNumber
        
    def getSegment(self):
        return ''.join(['IEA*', '*'.join([self.count, self.controlNumber]), '~'])
    
    