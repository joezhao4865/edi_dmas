from lib.ServiceLineHeader import *
from lib.ServiceDate import *
from lib.Contract import *
from lib.ServiceLine import *
from lib.Reference import *
from lib.ServiceLineList import *
from lib.Clients import *

class ServiceLines:
    def __init__(self, dilimiter, interchangeDate, patientID, liveIn, startDate, endDate, lineData):
        self.dilimiter = dilimiter
        #self.CONSTANT = Constant()
        self.dataList = lineData
        self.patientID = patientID
        self.rangedService = liveIn
        self.interchangeDate = interchangeDate
        #self.procedureCode = 'T1019' # data from lineData
        #self.units = 10 # data from lineData
        #self.billedAmt = '{:.2f}'.format(round(self.units * self.CONSTANT.HOURLY_RATE, 2)) 
        #self.seriveLocationZip = '22066' # data from lineData
        self.serviceStartDate = startDate # default to single claim. real data from lineData
        self.serviceEndDate = '' # single claim does not need end date
        #self.pcaFirstName = ''
        #self.pcaLastName = ''
        if liveIn:
            self.serviceStartDate = startDate
            self.serviceEndDate = endDate
        self.service_lines = ServiceLineList(dilimiter) # this is in claim file
    
    
    def get(self):
        for i in range(len(self.dataList)):
            repeatedService = self.dataList[i].modifier == '76'
            diagPointers = ':'.join([str(x) for x in range(1, len(Clients.clients[self.patientID]['diagcode'])+1)])
            Av_ServiceLineHeader = ServiceLineHeader(self.dilimiter, i+1, self.dataList[i].get_proc_code(), '{:.2f}'.format(self.dataList[i].get_units() * self.dataList[i].get_rate()), self.dataList[i].get_units(), self.dataList[i].get_zip(), diagPointers, self.rangedService, repeatedService).getSegment()
            
            Av_ServiceDate = ServiceDate(self.dataList[i].get_service_date(), self.rangedService, self.serviceEndDate).getSegment()
            Av_Contract = Contract().getSegment() # create an empty contract if it is not required
            Av_ClaimReference = Reference(True, '6R', self.interchangeDate+self.patientID+str(i+1)).getSegment()
            Av_ServiceLine = ServiceLine(self.dilimiter, Av_ServiceLineHeader, Av_ServiceDate, Av_ClaimReference, Av_Contract)
            self.service_lines.add(Av_ServiceLine.getSegment())
        return self.service_lines