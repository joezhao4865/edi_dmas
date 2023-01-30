class SubscriberDmg:
    def __init__(self, dob, sex):
        self.dmg01 = 'D8'
        self.dob = dob
        self.sex = sex
        
    def getSegment(self):
        return ''.join(['DMG*', '*'.join([self.dmg01, self.dob, self.sex]), '~'])