from lib.Constants import *
class Taxonomy:
    def __init__(self, qualifier, proc = ''):
        self.CONSTANT = Constant()
        self.prv01 = qualifier # code for submitter
        self.prv02 = 'PXC'  # entity not person which is 1
        self.prv03 = self.CONSTANT.PXC if proc == '' else self.CONSTANT.SVPXC[proc]
        
        
        
    def getSegment(self):
        return ''.join(['*'.join(['PRV', self.prv01, self.prv02, self.prv03]),  '~'])    