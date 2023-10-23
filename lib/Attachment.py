class Attachment:
    def __init__(self, need_attachment, controlnum, reportType = 'OZ', transmission = 'BM'):
        self.attach = need_attachment
        self.reportTypeCode = reportType
        self.transmissionCode = transmission
        self.pwk03 = ''
        self.pwk04 = ''
        self.pwk05 = 'AC'
        self.controlNumber = controlnum
        self.pwk07 = ''
        self.pwk08=''
        self.pwk09=''
    
    def getSegment(self):
        return ('', ''.join(['PWK*', '*'.join([self.reportTypeCode, self.transmissionCode, self.pwk03, self.pwk04, self.pwk05, self.controlNumber, self.pwk07, self.pwk08, self.pwk09]), '~']))[0 if not self.attach else 1]