class PickUp:
    def __init__(self, dilimiter, startAddress, endAddress):
        self.dilimiter = dilimiter
        self.pickup_nm101 = 'PW'
        self.pickup_nm102 = '2'
        self.dropoff_nm101 = '45'
        self.dropoff_nm102 = '2'
        self.startAddress = startAddress
        self.endAddress = endAddress
    
    def getSegment(self):
        return self.dilimiter.join([
            '*'.join(['NM1', self.pickup_nm101, self.pickup_nm102+'~']),
            self.startAddress,
            '*'.join(['NM1', self.dropoff_nm101, self.dropoff_nm102+'~']),
            self.endAddress
        ])