class Contract:
    def __init__(self, fundingSourceCode =''):
        self.contractType = '09'
        self.cn102 = ''
        self.cn103 = ''
        self.fundingSourceCode = fundingSourceCode
    
    def getSegment(self):
        return ('*'.join(['CN1', self.contractType, self.cn102, self.cn103, self.fundingSourceCode+'~']), '')[self.fundingSourceCode == '']