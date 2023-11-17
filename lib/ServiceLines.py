from lib.ServiceLineHeader import *
from lib.ServiceDate import *
from lib.Contract import *
from lib.ServiceLine import *
from lib.Reference import *
from lib.ServiceLineList import *
from lib.Clients import *
from lib.Address import *
from lib.Taxonomy import *
from lib.PCA import *
from lib.Attendant import *
from lib.PickUp import *
from datetime import datetime
class ServiceLines:
    def __init__(self, dilimiter, interchangeDate, patientID, starting_index, liveIn, startDate, endDate, lineData):
        self.dilimiter = dilimiter
        #self.CONSTANT = Constant()
        self.dataList = lineData
        self.patientID = patientID
        self.starting_index = starting_index
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
            v = self.dataList[i]
            repeatedService = v.modifier == '76'
            diagPointers = ':'.join([str(x) for x in range(1, len(Clients.clients[self.patientID]['diagcode'])+1)])
            
            Av_ServiceLineHeader = ServiceLineHeader(self.dilimiter, i+1, self.dataList[i].get_proc_code(), '{:.2f}'.format(v.get_billable()), v.get_units(), v.get_zip(), diagPointers, v.clock_in+'-'+v.clock_out, self.rangedService, repeatedService).getSegment()
            
            Av_ServiceDate = ServiceDate(v.get_service_date(), self.rangedService, self.serviceEndDate).getSegment()
            
            Av_Contract = Contract().getSegment() # create an empty contract if it is not required
            
            Av_ClaimReference = Reference(True, '6R', self.interchangeDate+self.starting_index + str(i)).getSegment()
            
            service_start_address = Address(True, self.dilimiter, v.startAddressline1, v.startAddressline2, v.startAddressCity, v.startAddressState, v.startAddressZip).getSegment()
            
            service_end_address = Address(True, self.dilimiter, v.endAddressline1, v.endAddressline2, v.endAddressCity, v.endAddressState, v.endAddressZip).getSegment()
            
            pickup = PickUp(self.dilimiter, service_start_address, service_end_address).getSegment()
            pca = PCA(self.dilimiter, Taxonomy('PE', v.proc).getSegment()).getSegment()
            spca = Attendant(self.dilimiter, v.pca_first, v.pca_last, v.pcaId).getSegment()
            Av_ServiceLine = ServiceLine(self.dilimiter, Av_ServiceLineHeader, Av_ServiceDate, Av_ClaimReference, pca, spca, pickup, Av_Contract)
            
            self.service_lines.add(Av_ServiceLine.getSegment())
        return self.service_lines