class HL_Subscriber_Availity:
    def __init__(self, hlChild = False, hlIndex = 2, parentIndex = 1):
        self.hlIndex = str(hlIndex)
        self.parentIndex = str(parentIndex)
        self.subscriberCode = '22'
        self.hlChild = ('0', '1')[hlChild]
    
    def getSegment(self):
        return ''.join(['HL*', '*'.join([self.hlIndex, self.parentIndex, self.subscriberCode, self.hlChild]),  '~'])