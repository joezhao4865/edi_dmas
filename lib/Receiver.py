class Receiver:
    def __init__(self, receiverName, receiverId):
        self.receiverName = receiverName
        self.receiverID = receiverId
        
    def getSegment(self):
        return ''.join(['NM1*', '*'.join(['40', '2', self.receiverName, '', '', '', '', '46', self.receiverID]),  '~'])