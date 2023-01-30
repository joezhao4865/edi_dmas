from lib.ClaimHeader import *
from lib.ServiceLines import *
from lib.Data_Availity import *
from lib.LeapYearChecker import *
from lib.SE_Availity import *

from datetime import datetime
import sys
import re

today = datetime.now()
currentYear = today.year
currentMonth = today.month
checkLeapYear = LeapYearChecker(currentYear)
monthEnds = {'1': 31, '2': (28, 29)[checkLeapYear.isLeapYear()], '3': 31, '4': 30, '5': 31, '6': 30, '7': 31, '8': 31, '9': 30, '10': 31, '11': 30, '12': 31}

payers = ['AETV', 'ANTV', 'MEDV', 'MAGV', 'VAVA', 'OPTV', 'UHTV']
payers.sort()

starting_index = '-1'
while int(starting_index) < 0 or int(starting_index) > 99999:
    starting_index = input('What is the starting index [0-99999]? ')
    if int(starting_index) < 0 or int(starting_index) > 99999:
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
    print(b 'please specify a valid value')
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
    service_month = str(currentMonth)
else:
    service_month = f'{service_month:0>2}'
    
service_start_date = input('What day did the service start (default to 1)? [1-31]? ')
while len(service_start_date.strip()) > 0 and not 1<= int(service_start_date) <= monthEnds[service_month]:
    print('Invalid date provided. Either go with the first day of the month or press Ctrl+c to terminate program')
    service_start_date = input('What day did the service start (default to 1)? [1-31]? ')
if len(service_start_date.strip()) == 0:
    service_start_date = '01'
else:   
    service_start_date = f'{service_start_date:0>2}'

service_end_date = input('What day did the service end (default to 1)? [1-31]? ')
while len(service_end_date.strip()) > 0 and (not 1<= int(service_end_date) <= monthEnds[service_month] or int(service_end_date) < int(service_start_date)):
    if int(service_end_date) < int(service_start_date):
        print('End date comes before start date')
    else:
        print('Invalid date provided. Either go with the last day of the month or press Ctrl+c to terminate program')
    service_end_date = input('What day did the service start (default to 1)? [1-31]? ')
if len(service_end_date.strip()) == 0:
    service_end_date = str(monthEnds[str(currentMonth)])
else:
    service_end_date = f'{service_end_date:0>2}'

serviceStart = ''.join([service_year, service_month, service_start_date])
serviceEnd = ''.join([service_year, service_month, service_end_date])
dilimiter = ('', '\n')[interchange_type in ['l', 'L']] 

# retrieve data from db. Proceed if data is returned otherwise exit
if client_medicaid_ID != '':
    # check start date and end date
    pass
else: 
    print(selectedPayer)


# for each client do the following if batch creation
claimHeader = ClaimHeader(dilimiter, starting_index, interchange_type, claim_freq_type, '')

(interchangeDate, subscriberID, resultList) = claimHeader.get()

serviceLines = ServiceLines(dilimiter, interchangeDate, subscriberID, is_live_in, serviceStart, serviceEnd, '')
resultList.append((serviceLines.get(), 'ServiceLines'))


###########################################
# merging each segment to make final data #
###########################################
outputData = Data_Availity(dilimiter, resultList)

traileressClaim = outputData.getAvailityData()

Av_SE = SE_Availity(traileressClaim.replace('\n', ''))

outputData.setSE(Av_SE.getSegment())

with open(interchangeDate+subscriberID+'.txt', 'w') as f:   
    f.write(outputData.getAvailityData())

print('next starting index: ' + str(int(starting_index) + 1))

