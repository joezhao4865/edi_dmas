class Reference:  
    def __init__(self, required = False, qualifier = '', medRcordNumber = ''):
        self.required = required
        self.qualifier = qualifier
        self.medicalRecordNumber = medRcordNumber
    
    def getSegment(self):
        return ('', '*'.join(['REF', self.qualifier, self.medicalRecordNumber+'~']))[self.required]
    
    def required(self):
        return self.required