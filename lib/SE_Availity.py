import re

class SE_Availity:
    def __init__(self, trailerLessClaim):
        self.claimString = trailerLessClaim
    
    
    def getSegment(self):
        stSegment = re.search(r'(ST[^~]+~)', self.claimString).groups(1)[0]
        stControlNumber = stSegment.split('*')[2]
        valueChunk = re.search(r'(ST.*GE\*)', self.claimString).groups(1)[0]
        #valueParts = valueChunk.split('~')
        segCount = len(valueChunk.split('~'))
        #for i, v in enumerate(valueParts, 1):
        #    print(str(i) + ' ' + v)
        #print(segCount)
        return ''.join(['*'.join(['SE', str(segCount), stControlNumber]), '~'])