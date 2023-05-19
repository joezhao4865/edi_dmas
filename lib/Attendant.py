from lib.Reference import *
from lib.Constants import *
from lib.Taxonomy import *
class Attendant:
    def __init__(self, dilimiter, firstname, lastname, pca_id):
        self.CONSTANT = Constant()
        self.dilimiter = dilimiter
        self.nm101 = 'DQ'
        self.nm102 = '1'
        self.pca_lastname = lastname
        self.pca_firstname = firstname
        #self.nm105 = ''
        #self.nm106 = ''
        #self.nm107 = ''
        #self.nm108 = 'XX'
        #self.nm109 = self.CONSTANT.NPI
        self.pcaref = Reference(True, 'LU', pca_id).getSegment()
        
    def getSegment(self):
        return self.dilimiter.join([
                '*'.join(['NM1', self.nm101, self.nm102, self.pca_lastname, self.pca_firstname+'~']),
                self.pcaref
            ])