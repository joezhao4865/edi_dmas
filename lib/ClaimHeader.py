from lib.Constants import *
from lib.Clients import *
from lib.ISA_Availity import *
from lib.IEA_Availity import *
from lib.GS_Availity import *
from lib.GE_Availity import *
from lib.ST_Availity import *
from lib.BHT_Availity import *
from lib.Constants import *
from lib.Submitter import *
from lib.SubmitterContact import *
from lib.Receiver import *
from lib.HL_Provider_Availity import *
from lib.BillingProvider import *
from lib.HL_Subscriber_Availity import *
from lib.SubscriberHeader import *
from lib.SubscriberName import *
from lib.Address import *
from lib.SubscriberDmg import *
from lib.Subscriber import *
from lib.Payer import *
from lib.Claim import *
from lib.Reference import *
from lib.HI import *
from lib.RenderingProvider import *
from lib.ServiceFacility import *
from lib.Taxonomy import *
from lib.Attachment import *

from datetime import datetime

class ClaimHeader:
    # pcaData should be a dict with keys: firstname and lastname
    def __init__(self, dilimiter, startingIndex, interchangeType, claimFreqType, total, sbrData, originalClaim, add_attachment, attachment_index, pcaData = ''):
        self.startingIndex = startingIndex
        self.dilimiter = dilimiter
        self.CONSTANT = Constant()
        self.subscriber = sbrData
        self.interchangeType = interchangeType
        self.pca = pcaData
        self.claimFreqType = claimFreqType
        self.billing_total = total
        self.headerList = []
        self.clientInfo = Clients.clients[sbrData.get_medicaid_id()]
        self.originalClaimID = originalClaim
        self.attachment = add_attachment
        self.attachmentIdx = attachment_index
        
    def get(self):
        ####################
        # Global variables #
        ####################
        proc_code = self.subscriber.get_proc_code()
        today = datetime.now() # for creating control number
        interchangeFullDate = ''.join([str(today.year), f'{today.month:0>2}', f'{today.day:0>2}'])
        interchangeDate = ''.join([str(today.year % 100), f'{today.month:0>2}', f'{today.day:0>2}'])
        interchangeTime = ''.join([f'{today.hour:0>2}', f'{today.minute:0>2}'])
        controlNumber = interchangeDate[-4:]+f'{self.startingIndex:0>5}'
        attachment_control_number = ''.join([self.subscriber.medicaidID, f'{today.month:0>2}', f'{today.day:0>2}', str(today.year), f'{self.attachmentIdx:0>5}']) if self.attachment else ''
        #############################
        # initializing each segment #
        #############################
        # ISA header and footer
        Av_ISA = ISA_Availity(interchangeDate, interchangeTime, controlNumber, self.interchangeType)
        Av_IEA = IEA_Availity('1', controlNumber)
        
        # GS/GE Segment
        Av_GS = GS_Availity(Av_ISA.getSenderId(), Av_ISA.getReceiverId(), interchangeFullDate, interchangeTime, controlNumber)
        Av_GE = GE_Availity('1', controlNumber)
        
        #ST Segment       
        # st control number starts with 0001 and increments by 1 per gs
        # bht control number start with 1 and increments by 1 per st
        Av_ST = ST_Availity(f'{self.startingIndex:0>5}', self.startingIndex)
        
        # BHT Segment
        Av_BHT = BHT_Availity(controlNumber, interchangeFullDate, interchangeTime)
        
        # 1000A loop
        # Submitter
        Av_Submitter = Submitter()
        
        # Submitter side contact info
        Av_Contact = SubmitterContact()
        
        # 1000B loop
        # Receiver info
        Av_Receiver = Receiver('Dept of Med Assist Svcs', Av_ISA.getReceiverId())
        
        # Billing Provider Hierarchical Level
        Av_HL_Provider = HL_Provider_Availity(self.dilimiter, proc_code, True, True)
        
        # Billing Provider Info
        Av_BillingProvider = BillingProvider(self.dilimiter)
        
        # Subscriber HL
        Av_SubscriberHL = HL_Subscriber_Availity()
        
        # Subscriber Info
        Av_SubscriberHeader = SubscriberHeader()
        Av_SubscriberName = SubscriberName(self.subscriber.get_medicaid_id(), self.subscriber.get_last_name(), self.subscriber.get_first_name())
        Av_SubscriberAddress = Address(True, self.dilimiter, self.subscriber.get_address1().strip(), self.subscriber.get_address2().strip(), self.subscriber.get_city().strip(), self.subscriber.get_state().strip(), self.subscriber.get_zip())
        Av_SubscriberDmg = SubscriberDmg(self.clientInfo['dob'], self.clientInfo['sex'])
        Av_Subscriber = Subscriber(Av_SubscriberHeader.getSegment(), Av_SubscriberName.getSegment(), Av_SubscriberAddress.getSegment(), Av_SubscriberDmg.getSegment(), self.dilimiter)
        
        
        # Payer Info
        Av_PayerAddress = Address(False, self.dilimiter, '12727 Fantasia Drive', '', 'Herndon', 'VA', '20170').getSegment()
        Av_Payer = Payer(self.dilimiter, 'VAMMIS FA', 'DMAS MEDICAID', Av_PayerAddress)
        
        # Claim Info
        Av_Claim = Claim(Av_SubscriberName.getPatientID(), self.billing_total, self.claimFreqType, self.subscriber.get_zip())
        Av_Attachment = Attachment(self.attachment, attachment_control_number)
        # Original Claim Reference. If this segment is required, set the first argument to 'True' and provide other info
        Av_MedicalReference = Reference(self.originalClaimID != '', 'F8', self.originalClaimID)
        Av_AuthReference = Reference(True, 'G1', self.subscriber.get_auth_number())
        # HI
        Av_HI = HI(self.clientInfo['diagcode'][0], self.clientInfo['diagcode'][1:])
        
        # Rendering provider (Optional) PCA part
        Av_RenderingProvider = RenderingProvider(True, self.dilimiter, Taxonomy('PE', proc_code).getSegment())
        #if self.pca != '':
        #    Av_RenderingProvider = RenderingProvider(True, self.pca['firstname'], self.pca['lastname'])
            
        
        # Service Facility (Optional) Becky healthcare might not need this field
        FacilityAddress = Address(True, self.dilimiter, self.CONSTANT.PROVIDER_ADDRESS1, self.CONSTANT.PROVIDER_ADDRESS2, self.CONSTANT.PROVIDER_CITY, self.CONSTANT.PROVIDER_STATE, self.CONSTANT.PROVIDER_ZIP)
        Av_ServiceFacility = ServiceFacility()
        
        headerList = [(Av_ISA, 'ISA'), (Av_IEA, 'IEA'), (Av_GS, 'GS'), (Av_GE, 'GE'), (Av_ST, 'ST'), (Av_BHT, 'BHT'), (Av_Submitter, 'Submitter'), (Av_Contact, 'Contact'), (Av_Receiver, 'Receiver'), (Av_HL_Provider, 'ProviderHL'), (Av_BillingProvider, 'ProviderInfo'), (Av_SubscriberHL, 'SubscriberHL'), (Av_Subscriber, 'Subscriber'), (Av_Payer, 'Payer'), (Av_Claim, 'Claim'), (Av_Attachment, 'Attachment'), (Av_HI, 'HI'), (Av_RenderingProvider, 'RenderingProvider'), (Av_ServiceFacility, 'ServiceFacility'), (Av_MedicalReference, 'MedicalReference'), (Av_AuthReference, 'AuthReference')]
        
        return (interchangeDate, Av_SubscriberName.getPatientID(), headerList)
                