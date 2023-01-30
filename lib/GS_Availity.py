class GS_Availity:
    def __init__(self, senderId, receiverId, createDateStr, createTimeStr, controlNumber):
        self.IDCode = 'HC'
        self.senderCode = senderId
        self.receiverCode = receiverId
        self.createDate = createDateStr
        self.createTime = createTimeStr
        self.controlNumber = controlNumber
        self.agencyCode = 'X'
        self.version = '005010X222A1'
    
    def getSegment(self):
        return ''.join(['GS*', '*'.join([self.IDCode, self.senderCode, self.receiverCode, self.createDate, self.createTime, self.controlNumber, self.agencyCode, self.version]), '~'])
       
        