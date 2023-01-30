class SubscriberName:
    def __init__(self, sbrID, lastName, firstName, middleName = '', suffix = '', idCode = 'MI'):
        self.entityIdCode = 'IL' # insured
        self.entityType = '1' # person
        self.lastName = lastName
        self.firstName = firstName
        self.middleName = middleName
        self.nm06 = ''
        self.suffix = suffix
        self.idCode = idCode
        self.subscriberID = sbrID
    
    def getSegment(self):
        return ''.join(['NM1*', '*'.join([self.entityIdCode, self.entityType, self.lastName, self.firstName, self.middleName, self.nm06, self.suffix, self.idCode, self.subscriberID]), '~'])
    
    def getPatientID(self):
        return self.subscriberID