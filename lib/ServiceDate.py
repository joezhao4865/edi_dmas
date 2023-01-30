class ServiceDate:  
    def __init__(self, serviceStart, rangedService = False, serviceEnd = ''):
        self.dtp01 = '472'
        self.dtp02 = ('D8', 'RD8')[rangedService]
        self.serviceDate = serviceStart + ('', '-'+serviceEnd)[rangedService]
    
    def getSegment(self):
        return ''.join(['*'.join(['DTP', self.dtp01, self.dtp02, self.serviceDate]), '~'])