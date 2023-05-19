class Data_Availity:
    def __init__(self, dilimiter, segments):
        self.dilimiter = dilimiter
        self.ISA = ''
        self.IEA = ''
        self.GS = ''
        self.GE = ''
        self.ST = ''
        self.BHT = ''
        self.Submitter = ''
        self.Contact = ''
        self.Receiver = ''
        self.ProviderHL = ''
        self.ProviderInfo = ''
        self.SubscriberHL = ''
        self.Subscriber = ''
        self.Payer = ''
        self.Claim = ''
        self.MedicalReference = ''
        self.AuthReference = ''
        self.HI = ''
        self.RenderingProvider = ''
        self.ServiceFacility = ''
        self.ServiceLines = ''
        self.SE = ''
        self.segments = [] # this is the array storing the resulting segment strings
        self.setSegmentsData(segments) 
        
        
    def getAvailityData(self):
        self.mergeSegments()
        return self.dilimiter.join(self.segments)
        
    def setSegmentsData(self, segments):
        for seg in segments:
            setattr(self, seg[1], seg[0].getSegment())
        
    
    def mergeSegments(self):
        self.segments = [self.ISA, self.GS, self.ST, self.BHT, self.Submitter, self.Contact, self.Receiver, self.ProviderHL, self.ProviderInfo, self.SubscriberHL, self.Subscriber, self.Payer, self.Claim]
        
        if self.MedicalReference != '':
            self.segments.append(self.MedicalReference)
            
        self.segments.append(self.AuthReference)
        self.segments.append(self.HI)
        
        if self.RenderingProvider != '':
            self.segments.append(self.RenderingProvider)
        
        if self.ServiceFacility != '':
            self.segments.append(self.ServiceFacility)
            
        self.segments.extend([self.ServiceLines, self.SE, self.GE, self.IEA])
    
    
    def setSE(self, seSegment):
        self.SE = seSegment