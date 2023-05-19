class Address:
    def __init__(self, required = False, dilimiter='', address1='', address2='', city='', state='', zip=''):
        self.required = required
        self.dilimiter = dilimiter
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.state = state.strip(' ')
        self.zip = zip
    
    def getSegment(self):
        return  ('', self.dilimiter.join([''.join(['N3*', self.address1+ ('', ' ' + self.address2)[self.address2 !=''], '~']), ''.join(['N4*', '*'.join([self.city, self.state, self.zip]), '~'])]))[self.required == True]