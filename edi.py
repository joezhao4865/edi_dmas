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
                shutil.copy(newpath, destpath)
            else:
                CollectFiles(newpath, destpath)

today = datetime.now()
currentYear = today.year
currentMonth = today.month
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

service_year = input('Whcih year is the claim for (please enter a full year and up to last 3 years)? ')
while len(service_year.strip()) > 0 and (not re.match(r'\d\d\d\d', service_year) or int(service_year) > currentYear or int(service_year) < currentYear - 3):
    print('Invalid year value provided. Either go with current year or press Ctrl+c to terminate program')
    service_year = input('Whcih year is the claim for (please enter a full year and up to last 3 years)? ')
if len(service_year.strip()) == 0:
    service_year = str(currentYear)

service_month = input('Whcih month is the claim to be created (default to current month) [1-12]? ')
while len(service_month.strip()) > 0 and (int(service_month) < 1 or int(service_month) > 12):
    service_month = input('Whcih month is the claim to be created (default to current month) [1-12]? ')
if len(service_month.strip()) == 0:
    service_month = f'{currentMonth:0>2}'
else:
    service_month = f'{service_month:0>2}'
    
service_start_date = input('What day did the service start (default to 1)? [1-31]? ')
while len(service_start_date.strip()) > 0 and not 1<= int(service_start_date) <= monthEnds[service_month.lstrip('0')]:
    print('Invalid date provided. Either go with the first day of the month or press Ctrl+c to terminate program')
    service_start_date = input('What day did the service start (default to 1)? [1-31]? ')
if len(service_start_date.strip()) == 0:
    service_start_date = '01'
else:   
    service_start_date = f'{service_start_date:0>2}'

service_end_date = input('What day did the service end (default to 1)? [1-31]? ')
while len(service_end_date.strip()) > 0 and (not 1<= int(service_end_date) <= monthEnds[service_month.lstrip('0')] or int(service_end_date) < int(service_start_date)):
    if int(service_end_date) < int(service_start_date):
        print('End date comes before start date')
    else:
        print('Invalid date provided. Either go with the last day of the month or press Ctrl+c to terminate program')
    service_end_date = input('What day did the service end (default to 1)? [1-31]? ')
if len(service_end_date.strip()) == 0:
    service_end_date = str(monthEnds[str(currentMonth).lstrip('0')])
else:
    service_end_date = f'{service_end_date:0>2}'

serviceStart = ''.join([service_year, service_month, service_start_date])
serviceEnd = ''.join([service_year, service_month, service_end_date])
dilimiter = ('', '\n')[interchange_type in ['l', 'L']] 

visits = {}
parentDir = ''
conn = connector('beckycare')
connection = conn.getConnection()
cursor = connection.cursor()
# retrieve data from db. Proceed if data is returned otherwise exit
try:
    sql = 'select recipient_first_name, recipient_last_name, procedure_code, service_date, payer_code, work_units, unit_rate, modifier, service_address1, service_address2, service_city, service_state, service_zip, medicaid_id, auth_number from visits_staging'
    
    if client_medicaid_ID != '':
        sql = sql + ' where medicaid_id = ' + client_medicaid_ID    
    else: 
        sql = sql + ' where payer_code = \'' + selectedPayer + '\''
        
    sql = sql + ' and service_date between \'' + serviceStart + '\' and \'' + serviceEnd + '\' order by service_date'
    cursor.execute(sql)    
    for row in cursor.fetchall():
        visit = Visit(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14])
        if not visit.get_medicaid_id() in visits:
            visits[visit.get_medicaid_id()] = []
        visits[visit.get_medicaid_id()].append(visit)
finally:
    cursor.close()
    conn.close()



# for each client do the following if batch creation
for key in visits.keys():
    total_billed = sum([v.get_units() * v.get_rate() for v in visits[key]])
    claimHeader = ClaimHeader(dilimiter, starting_index, interchange_type, claim_freq_type, total_billed, visits[key][0])

    (interchangeDate, subscriberID, resultList) = claimHeader.get()

    serviceLines = ServiceLines(dilimiter, interchangeDate, subscriberID, is_live_in, serviceStart, serviceEnd, visits[key])
    resultList.append((serviceLines.get(), 'ServiceLines'))

    ###########################################
    # merging each segment to make final data #
    ###########################################
    outputData = Data_Availity(dilimiter, resultList)

    traileressClaim = outputData.getAvailityData()

    Av_SE = SE_Availity(traileressClaim.replace('\n', ''))

    outputData.setSE(Av_SE.getSegment())
    starting_index = str(int(starting_index) + len(visits[key]))
    
    parent = ('Originals', 'Appeals', 'Cancels')[0 if claim_freq_type  == '1' else 1 if claim_freq_type == '7' else 2]
    parentDir = 'C:\\Users\Becky\\Desktop\\claims\\MEDV\\' + parent + '\\' + interchangeDate 
    storagePath = parentDir + '\\' + visits[key][0].get_first_name() + '_' + visits[key][0].get_last_name()
    if not os.path.exists(storagePath):
        os.makedirs(storagePath)
    with open(storagePath + '\\' + interchangeDate+'_'+subscriberID+'.txt', 'w') as f:   
        f.write(outputData.getAvailityData())


CollectFiles(parentDir, parentDir)
        
print('next starting index: ' + str(int(starting_index)))


