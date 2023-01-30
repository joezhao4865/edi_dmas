from lib.Constants import *

class ISA_Availity:
    #params: interchangeDate: string length 8
    #        interchangeTime: string length 4
    #        sender assigned control number has to be identical to IEA02: string length 9
    #        submission type: 'P' or 'T'
    def __init__(self, interchangeDate, interchangeTime, controlNumber, changeType):
        self.CONSTANT = Constant()
        self.isa01 = '00'
        self.isa02 = ' '*10
        self.isa03 = '00'
        self.isa04 = ' '*10
        self.isa05 = 'ZZ'
        self.isa06_1 = self.CONSTANT.SENDERID
        self.isa06 = self.isa06_1 + ' '*(15-len(self.isa06_1))
        self.isa07 = 'ZZ'
        self.isa08_1 = 'VAMMIS FA'
        self.isa08 = self.isa08_1 + ' '*(15-len(self.isa08_1))
        self.isa09 = interchangeDate
        self.isa10 = interchangeTime
        self.isa11 = '^'
        self.isa12 = '00501'
        self.isa13 = controlNumber
        self.isa14 = '0'
        #elf.isa15 = changeType.upper()
        self.isa15 = ('P', 'T')[changeType.upper() in ['L', 'T']]
        self.isa16 = ':'
        self.isa = []
    
    def __setISA(self):
        self.isa = [self.isa01, self.isa02, self.isa03, self.isa04, self.isa05, self.isa06, self.isa07, self.isa08, self.isa09, self.isa10, self.isa11, self.isa12, self.isa13, self.isa14, self.isa15, self.isa16]
    
    def getSegment(self):
        self.__setISA()
        return ''.join(['ISA*', '*'.join(self.isa),  '~'])
        
    def getControlNumber(self):
        return self.isa13
    
    def getSenderId(self):
        return self.isa06_1
    
    def getReceiverId(self):
        return self.isa08_1
    
    def getBillerID(self):
        return self.CONSTANT.AETVBILLERID
    
    def getInterchangeDate(self):
        return self.isa09
   