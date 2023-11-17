class Visit:
    def __init__(self, pcafirst, pcalast, pcaId, firstname, lastname, proc, service_date, payer, work_units, adjusted_units, unit_rate, billed_amount, modifier, service_address1, service_address2, service_city, service_state, service_zip, end_address1, end_address2, end_city, end_state, end_zip, medicaid_id, auth_number, clockIn, clockOut):
        self.pca_first = pcafirst
        self.pca_last = pcalast
        self.pcaId = pcaId
        self.firstname = firstname
        self.lastname = lastname
        self.proc = proc
        self.service_date = service_date.replace('-', '')
        self.payer = payer
        self.units = work_units
        self.adjusted_units = adjusted_units
        self.rate = unit_rate
        self.billable_amount = billed_amount
        self.modifier = modifier
        self.startAddressline1 = service_address1
        self.startAddressline2 = service_address2
        self.startAddressCity = service_city
        self.startAddressState = service_state
        self.startAddressZip = service_zip
        self.endAddressline1 = end_address1
        self.endAddressline2 = end_address2
        self.endAddressCity = end_city
        self.endAddressState = end_state
        self.endAddressZip = end_zip
        self.medicaidID = medicaid_id
        self.authNumber = auth_number
        self.clock_in = clockIn
        self.clock_out = clockOut
        
    def get_first_name(self):
        return self.firstname
    def get_last_name(self):
        return self.lastname
    def get_proc_code(self):
        return self.proc
    def get_service_date(self):
        return self.service_date
    def get_payer(self):
        return self.payer
    def get_units(self):
        return self.units
    def get_rate(self):
        return self.rate
    def get_modifier(self):
        return self.modifier
    def get_address1(self):
        return self.startAddressline1
    def get_address2(self):
        return self.startAddressline2
    def get_city(self):
        return self.startAddressCity
    def get_state(self):
        return self.startAddressState
    def get_zip(self):
        return self.endAddressZip
    def get_medicaid_id(self):
        return self.medicaidID
    def get_auth_number(self):
        return self.authNumber
    def get_billable(self):
        return self.billable_amount
    