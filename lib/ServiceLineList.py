class ServiceLineList:
    def __init__(self, dilimiter):
        self.dilimiter = dilimiter
        self.lines = []
    
    def add(self, serviceLine):
        self.lines.append(serviceLine)
    
    def addRange(self, lineList):
        self.lines.extend(lineList)
    
    def getSegment(self):
        if len(self.lines) > 0:
            return self.dilimiter.join(self.lines)
        else:
            return ''