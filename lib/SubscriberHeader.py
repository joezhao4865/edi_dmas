class SubscriberHeader:
    def __init__(self, sbrType = 'P', sbrRel = '18', clmFiling = 'MC'):
        self.sbrType = sbrType
        self.sbrRel = sbrRel
        self.sbr03 = ''
        self.sbr04 = ''
        self.sbr05 = ''
        self.sbr06 = ''
        self.sbr07 = ''
        self.sbr08 = ''
        self.clmFilingCode = clmFiling
    
    def getSegment(self):
        return ''.join(['SBR*', '*'.join([self.sbrType, self.sbrRel, self.sbr03, self.sbr04, self.sbr05, self.sbr06, self.sbr07, self.sbr08, self.clmFilingCode]), '~'])