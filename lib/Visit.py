class Visit:
	def __init__(self, firstname, lastname, proc, service_date, payer, work_units, unit_rate, modifier, service_address1, service_address2, service_city, service_state, service_zip, medicaid_id, auth_number):
		self.firstname = firstname
		self.lastname = lastname
		self.proc = proc
		self.service_date = service_date.replace('-', '')
		self.payer = payer
		self.units = work_units
		self.rate = unit_rate
		self.modifier = modifier
		self.address1 = service_address1
		self.address2 = service_address2
		self.city = service_city
		self.state = service_state
		self.zip = service_zip
		self.medicaidID = medicaid_id
		self.authNumber = auth_number
	
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
		return self.address1
	def get_address2(self):
		return self.address2
	def get_city(self):
		return self.city
	def get_state(self):
		return self.state
	def get_zip(self):
		return self.zip
	def get_medicaid_id(self):
		return self.medicaidID
	def get_auth_number(self):
		return self.authNumber
	