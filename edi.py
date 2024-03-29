from lib.ServiceLines import *
from lib.Data_Availity import *
from lib.LeapYearChecker import *
from lib.SE_Availity import *
from lib.ClaimHeader import *
from lib.Connecter import *
from datetime import datetime
from lib.Visit import *
from decimal import *
from lib.Clients import *
import shutil
import os
import sys
import re


def CollectFiles(rootpath, destpath):
    if rootpath != '':
        for file in os.listdir(rootpath):
            newpath = rootpath+'\\'+file
            if os.path.isfile(newpath):
                if not os.path.exists(destpath + '\\' + file):
                    shutil.copy(newpath, destpath)
            else:
                CollectFiles(newpath, destpath)

def time_to_string(date1):
    return ''.join(str(date1).split(' ')[1].split(':')[:2])

def clean_file(file_content):
    return re.sub(r'\*+~', '~', file_content)

claimToReplace = ''
today = datetime.now()
currentYear = today.year
currentMonth = today.month
currentTime= re.sub(r':', '', str(today.time()).split('.')[0])
checkLeapYear = LeapYearChecker(currentYear)
monthEnds = {'1': 31, '2': (28, 29)[checkLeapYear.isLeapYear()], '3': 31, '4': 30, '5': 31, '6': 30, '7': 31, '8': 31, '9': 30, '10': 31, '11': 30, '12': 31}

payers = ['AETV', 'ANTV', 'MEDV', 'MAGV', 'VAVA', 'OPTV', 'UHTV']
payers.sort()

starting_index = '-1'
while int(starting_index) < 1 or int(starting_index) > 99999:
    starting_index = input('What is the starting index [1-99999]? ')
    if int(starting_index) < 1 or int(starting_index) > 99999:
        print('Invalid starting index provided')
        
interchange_type = ''
while not interchange_type in ['l', 'L', 't', 'T', 'p', 'P']:
    interchange_type = input('What is the interchange type [\'l\', \'L\', \'t\', \'T\', \'p\', \'P\']? ')
    if not interchange_type in ['l', 'L', 't', 'T', 'p', 'P']:
        print('Invalid type provided')
        
is_live_in = ''
while not is_live_in in ['0', '1']:
    is_live_in = input('Is this a live-lin claim [0/1]? ')
    if not is_live_in in ['0', '1']:
        print('Invalid live_in indicator provided')

is_live_in = bool(int(is_live_in))

single_batch = ''
while not single_batch in ['s', 'b']:
    single_batch = input('Is this a single claim for a batch claim request [\'s\', \'b\']? ' )
    if not single_batch in ['s', 'b']:
        print('Invalid single/batch claim indicator provided')
        
claim_freq_type = input('what is the claim frequency type [original/default = 1, replacement = 7, cancel/void = 8]? ')
while not claim_freq_type.strip() in ['', '1', '7', '8']:
    print('please specify a valid value')
    claim_freq_type = input('what is the claim frequency type [origial/default = 1, replacement = 7, cancel/void = 8]? ')
    if claim_freq_type.strip() == '':
        claim_freq_type = '1'
        
if claim_freq_type.strip() in ['7','8']:
    claimToReplace = input('Original Claim ID: ')
    while claimToReplace.strip() == '':
        claimToReplace = input('Original Claim ID: ')

need_attachment = input('Do you need submit attachment [Y|N]')
attachment = False
attachment_index = ''
while need_attachment != '' and not re.match(r'[YyNn]', need_attachment.strip()):
    print("please type 'Y' or 'N'")
    need_attachment = input('Do you need submit attachment [Y|N]')
if need_attachment.lower() in ['y', 'yes', 'ye', 'yup', 'yeah']:
    attachment = True
    attachment_index = input('Enter attachment file index [1-99999]')
    while not re.match(r'^\d{1,5}$', attachment_index.strip()):
        print('Please enter a number between 1 and 99999')
        attachment_index = input('Enter attachment file index [1-99999]')

selectedPayer = ''
if single_batch.strip() == 'b':
    payerOptions = []
    for i, v in enumerate(payers, 1):
        payerOptions.append(str(i))
        if i % 4 == 0:  
            print(str(i)+'-'+v)
        else:
            print('\t' + str(i)+'-'+v, end='   ')
    payerIndex = input('\nplease specify a payer from the list above ')
    while not payerIndex in payerOptions:
        payerIndex = input('please specify a payer from the list above ')
    selectedPayer = payers[int(payerIndex)-1]

client_medicaid_ID = ''   
if single_batch.strip() == 's':
    while client_medicaid_ID == '':
        client_medicaid_ID = input("What is the client's medicaid ID? " )
        if client_medicaid_ID == '':
            print('Please provide client medicaid ID')

validDate = False
while not validDate:
    validDate = True
    service_start_date = input('Service start date - YYMMDD: ').strip()
    if service_start_date == '':
        validDate = True
    elif re.match(r'\d{6}$', service_start_date):
        year = 2000 + int(service_start_date[:2])
        month = service_start_date[2:4].strip('0')
        date = int(service_start_date[-2:])
        if month in ['1','3','4','5','6','7','8','9','10','11','12'] and (date > monthEnds[month] or date < 1):
            print('Wrong date of month')
            validDate = False
        elif int(month) < 1 or int(month) > 12:
            print('Wrong month of year')
            validDate = False
        elif year > currentYear:
            print('No future date will be considered')
            validDate = False
        elif year < currentYear - 3:
            print('Only dates in last 3 years allowed')
            validDate = False
        elif month == '2':
            if date > 29 or date == 29 and not LeapYearChecker(year).isLeapYear():
                print('Invalid date in Februrary')
                validDate = False       
    else:
        print('Invalid date value')
        validDate = False
if service_start_date == '':
    print(today.date)
    service_start_date = str(currentYear)+f'{currentMonth:0>2}'+f'{today.day:0>2}'
else:
    service_start_date = '20' + service_start_date

validDate = False
while not validDate:
    validDate = True
    service_end_date = input('Service end date - YYMMDD: ').strip()
    if service_end_date == '':
        validDate = True
    elif re.match(r'\d{6}$', service_end_date):
        year = 2000 + int(service_end_date[:2])
        month = service_end_date[2:4].strip('0')
        date = int(service_end_date[-2:])
        if month in ['1','3','4','5','6','7','8','9','10','11','12'] and (date > monthEnds[month] or date < 1):
            print('Wrong date of month')
            validDate = False
        elif int(month) < 1 or int(month) > 12:
            print('Wrong month of year')
            validDate = False
        elif year > currentYear:
            print('No future date will be considered')
            validDate = False
        elif year < currentYear - 3:
            print('Only dates in last 3 years allowed')
            validDate = False
        elif month == '2':
            if date > 29 or date == 29 and not LeapYearChecker(year).isLeapYear():
                print('Invalid date in Februrary')
                validDate = False
        elif int(service_end_date) < int(service_start_date[2:]):
            print('Service end date should be after start date')
            validDate = False
    else:
        print('Invalid date value')
        validDate = False
if service_end_date == '':
    service_end_date = service_start_date
else:
    service_end_date = '20' + service_end_date

service_type = input('Service type: ').strip()


dilimiter = ('', '\n')[interchange_type in ['l', 'L']] 

visits = {}
parentDir = ''
conn = connector('beckycare')
connection = conn.getConnection()
cursor = connection.cursor()
# retrieve data from db. Proceed if data is returned otherwise exit
try:
    sql = 'select pca_first_name, pca_last_name, pca_username, recipient_first_name, recipient_last_name, procedure_code, service_date, payer_code, work_units, adjusted_units, unit_rate, billable_amount, modifier, service_address1, service_address2, service_city, service_state, service_zip, end_address1, end_address2, end_city, end_state, end_zip, medicaid_id, auth_number, clock_in, clock_out from visits_staging'
    
    if client_medicaid_ID != '':
        sql = sql + ' where medicaid_id = \'' + client_medicaid_ID + '\''  
    else: 
        sql = sql + ' where payer_code = \'' + selectedPayer + '\''
        
    sql = sql + ' and service_date between \'' + service_start_date + '\' and \'' + service_end_date + '\''
    #sql = sql + ' group by recipient_first_name, recipient_last_name, procedure_code, service_date, payer_code, unit_rate,  service_address1, service_address2, service_city, service_state, service_zip, medicaid_id, auth_number'
    if service_type != '':
        sql = sql + ' and procedure_code = \'' + service_type + '\''
    sql = sql + ' order by service_date'
    
    cursor.execute(sql)    
    for row in cursor.fetchall(): 
        clockInTime, clockOutTime = time_to_string(row[25]), time_to_string(row[26]), 
        visit = Visit(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24], clockInTime, clockOutTime)
        
        med_id = visit.get_medicaid_id() + ':' + visit.get_proc_code()
        if not med_id in visits:
            visits[med_id] = []            
        visits[med_id].append(visit) 
finally:
    cursor.close()
    conn.close()



# for each client do the following if batch creation
for key in visits.keys():
    proc_code = key.split(':')[1]
    total_billed = sum([v.get_billable() for v in visits[key]])
    claimHeader = ClaimHeader(dilimiter, starting_index, interchange_type, claim_freq_type, total_billed, visits[key][0], claimToReplace, attachment, attachment_index)

    (interchangeDate, subscriberID, resultList) = claimHeader.get()

    serviceLines = ServiceLines(dilimiter, interchangeDate, subscriberID, starting_index, is_live_in, service_start_date, service_end_date, visits[key])
    resultList.append((serviceLines.get(), 'ServiceLines'))

    ###########################################
    # merging each segment to make final data #
    ###########################################
    outputData = Data_Availity(dilimiter, resultList)

    traileressClaim = outputData.getAvailityData()

    Av_SE = SE_Availity(traileressClaim.replace('\n', ''))

    outputData.setSE(Av_SE.getSegment())
    starting_index = str(int(starting_index) + len(visits[key]))
    
    if interchange_type in ['p', 'P']:
        parent = ('Originals', 'Appeals', 'Cancels')[0 if claim_freq_type  == '1' else 1 if claim_freq_type == '7' else 2]
        parentDir = re.sub(r'\\', '\\\\\\\\', os.path.expanduser('~'))+'\\Documents\\claims\\MEDV\\' + parent + '\\' + interchangeDate 
        storagePath = parentDir + '\\' + visits[key][0].get_first_name() + '_' + visits[key][0].get_last_name()
        if not os.path.exists(storagePath):
            os.makedirs(storagePath)
        with open(''.join([storagePath,'\\',interchangeDate,'_',visits[key][0].get_first_name()[0],visits[key][0].get_last_name()[0],proc_code,currentTime,interchange_type.upper(),'.txt']), 'w') as f:   
            f.write(clean_file(outputData.getAvailityData()))
    else:   
        print(clean_file(outputData.getAvailityData()))

if interchange_type in ['p', 'P']:
    CollectFiles(parentDir, parentDir)
        
print('next starting index: ' + starting_index)

