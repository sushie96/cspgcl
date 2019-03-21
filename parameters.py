database_file = 'CSPGCL_funds_database.db'

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

release_funds_format = []
release_funds_format.append(['r_date', 'datetime', 'NOT NULL',''])
release_funds_format.append(['r_amount', 'text', 'NOT NULL', ''])
release_funds_format.append(['r_transaction_id', 'text', 'NOT NULL', 'PRIMARY KEY'])

release_funds_format.append(['fund_left', 'text', 'NOT NULL', ''])

class release_funds:
	def __init__(self, r_date, r_amount, r_transaction_id):
		self.r_date = r_date
		self.r_amount = r_amount
		self.r_transaction_id = r_transaction_id
		self.fund_left = fund_left

	def output_dict(self):
		val_dict = {'r_date':self.r_date, 'r_amount':self.r_amount, 'r_transaction_id':self.r_transaction_id, 'fund_left':self.fund_left}
		return val_dict

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

payment_bill_format = []
payment_bill_format.append(['issue_date', 'datetime', 'NOT NULL', ''])
payment_bill_format.append(['due_date', 'datetime', 'NOT NULL', ''])	
payment_bill_format.append(['b_type', 'text', 'NOT NULL', ''])
payment_bill_format.append(['p_amount', 'text', 'NOT NULL', ''])
payment_bill_format.append(['pb_transaction_id', 'text', 'NOT NULL', 'PRIMARY KEY'])

payment_bill_format.append(['p_amount_left', 'text', 'NOT NULL', ''])
payment_bill_format.append(['p_surcharge_left', 'text', 'NOT NULL', ''])
payment_bill_format.append(['p_other_charges_left', 'text', 'NOT NULL', ''])

class payment_bill:
	def __init__(self, issue_date, due_date, b_type, p_amount, p_amount_left, p_surcharge_left, p_other_charges_left, pb_transaction_id):
		self.issue_date = issue_date
		self.due_date = due_date
		self.b_type = b_type
		self.p_amount = p_amount
		self.p_amount_left = p_amount_left
		self.p_surcharge_left = p_surcharge_left
		self.p_other_charges_left = p_other_charges_left
		self.pb_transaction_id = pb_transaction_id

	def output_dict(self):
		val_dict = {'issue_date':self.issue_date, 'due_date':self.due_date, 'b_type':self.b_type, 'p_amount':self.p_amount}
		val_dict.update({'pb_transaction_id':self.pb_transaction_id})
		val_dict.update({'p_amount_left':self.p_amount_left, 'p_surcharge_left':self.p_surcharge_left, 'p_other_charges_left':self.p_other_charges_left})
		return val_dict

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

payments_format = []
payments_format.append(['issue_date', 'datetime', 'NOT NULL', ''])
payments_format.append(['due_date', 'datetime', 'NOT NULL', ''])
payments_format.append(['b_type', 'text', 'NOT NULL', ''])
payments_format.append(['p_amount', 'text', 'NOT NULL', ''])
payments_format.append(['p_amount_left', 'text', 'NOT NULL', ''])
payments_format.append(['p_surcharge_left', 'text', 'NOT NULL', ''])
payments_format.append(['p_other_charges_left', 'text', 'NOT NULL', ''])
payments_format.append(['fund_left', 'text', 'NOT NULL', ''])
payments_format.append(['paid_date', 'datetime', 'NOT NULL', ''])
payments_format.append(['r_transaction_id', 'text', 'NOT NULL', ''])
payments_format.append(['pb_transaction_id', 'text', 'NOT NULL', ''])

class payments:
	def __init__(self, issue_date, due_date, b_type, p_amount, p_amount_left, p_surcharge_left, p_other_charges_left, fund_left, paid_date, r_transaction_id, pb_transaction_id):
		self.issue_date = issue_date
		self.due_date = due_date
		self.b_type = b_type
		self.p_amount = p_amount
		self.p_amount_left = p_amount_left
		self.p_surcharge_left = p_surcharge_left
		self.p_other_charges_left = p_other_charges_left
		self.fund_left = fund_left
		self.paid_date = paid_date
		self.r_transaction_id = r_transaction_id
		self.pb_transaction_id = pb_transaction_id

		def output_dict(self):
			val_dict = {'issue_date':self.issue_date, 'due_date':self.due_date, 'b_type':self.b_type, 'p_amount':self.p_amount}
			val_dict.update({'p_amount_left':self.p_amount_left, 'p_surcharge_left':self.p_surcharge_left, 'p_other_charges_left':self.p_other_charges_left})
			val_dict.update({'fund_left':self.fund_left, 'paid_date':self.paid_date, 'r_transaction_id':self.r_transaction_id, 'pb_transaction_id':self.pb_transaction_id})
			return val_dict

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

bill_type_format = []
bill_type_format.append(['b_type', 'text', 'NOT NULL', 'PRIMARY KEY'])
bill_type_format.append(['days', 'integer', 'NOT NULL', ''])
bill_type_format.append(['rate', 'real', 'NOT NULL', ''])

class bill_type:
	def __init__(self, b_type, days, rate):
		self.b_type = b_type
		self.days = days
		self.rate = rate
		
	def output_dict(self):
		val_dict = {'b_type':self.b_type, 'days':self.days, 'rate':self.rate}
		return val_dict

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

		