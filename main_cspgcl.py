from parameters import *
from database import *

from datetime import date
from datetime import timedelta
from datetime import datetime

from operator import itemgetter
import hashlib

from lib_cspgcl import *

def create_table_main():
	create_table(database_file, 'Released_Funds', release_funds_format)
	create_table(database_file, 'Payment_Bills', payment_bill_format)
	create_table(database_file, 'Payments', payments_format)
	create_table(database_file, 'Bill_Type', bill_type_format)

def payment_bill_details():
	cls_screen()
	print("=============================================================")
	print("               Entering Payment Bill Details")
	print("=============================================================")
	print()
	i_issue_date_year = int(input("\tEnter Payment Issue Year:   "))
	i_issue_date_month = int(input("\tEnter Payment Issue Month:   "))
	i_issue_date_day = int(input("\tEnter Payment Issue Day:   "))
	i_b_type = input("\tEnter Bill Type (D/T/R):   ")
	i_p_amount = input("\tEnter Principal Amount:   ")
	i_issue_date = date(i_issue_date_year, i_issue_date_month, i_issue_date_day)
	delta_days_list_all = retrieve_table(database_file, 'Bill_Type', 'days', 'b_type = "' + i_b_type + '"')
	delta_days = extract_data_from_sql(delta_days_list_all)
	i_due_date = i_issue_date + timedelta(delta_days)
	# i_pb_transaction_id = hashlib.md5(datetime.now().strftime('%Y%m%d%H%M%S%f').encode()).hexdigest()
	i_pb_transaction_id = datetime.now().strftime('%Y-%m-%d::%H:%M:%S:%f')

	print(i_pb_transaction_id)
	insert_data(database_file, 'Payment_Bills', payment_bill_format, [i_issue_date, i_due_date, i_b_type, i_p_amount, i_pb_transaction_id, i_p_amount, 0, 0])
	print()
	print()
	exit_menu = input("Press Any Key To Continue...")

def released_fund_details():
	cls_screen()
	print("=============================================================")
	print("               Entering Released Fund Details")
	print("=============================================================")
	print()
	i_r_date_year = int(input("\tEnter Released Funds Issue Year:   "))
	i_r_date_month = int(input("\tEnter Released Funds Issue Month:   "))
	i_r_date_day = int(input("\tEnter Released Funds Issue Day:   "))
	i_r_amount = input("\tEnter Released Amount:   ")
	i_r_transaction_id = input("\tEnter Transaction ID:   ")
	i_r_date = date(i_r_date_year, i_r_date_month, i_r_date_day)
	insert_data(database_file, 'Released_Funds', release_funds_format, [i_r_date, i_r_amount, i_r_transaction_id, i_r_amount])
	print()
	print()
	exit_menu = input("Press Any Key To Continue...")

def settle_bills(settle_date):
	cls_screen()
	print("=============================================================")
	print("                      Settling Bills")
	print("=============================================================")
	print()
	
	current_date = settle_date
	payment_bill_data=retrieve_table(database_file, 'Payment_Bills', '*', 'p_amount_left != 0')
	payment_bill_data = sorted(payment_bill_data,key=itemgetter(1))
	for i in payment_bill_data:
		print(i)
	released_funds_data=retrieve_table(database_file, 'Released_Funds', '*', 'fund_left != 0')
	for i in released_funds_data:
		print(i)

	# -----------------------------------------------------------------------------------------------------------------------------------
	
	payment_bill_data=retrieve_table(database_file, 'Payment_Bills', '*', 'p_amount_left != 0')
	payment_bill_data = sorted(payment_bill_data,key=itemgetter(1))

	released_funds_iter = iter(released_funds_data)
	payment_bill_iter = iter(payment_bill_data)
	
	fund = 0
	charge_list = {'Surcharge':0, 'Other':0, 'Principal':0}

	pb_item = 0
	rf_item = 0

	while True:
		try:
			if charge_list['Principal'] == 0:
				print()
				pb_item = next(payment_bill_iter)
				bill_type = pb_item[2]
				rate = retrieve_table(database_file, 'Bill_Type', 'rate', "b_type = '" + bill_type + "'")
				rate = extract_data_from_sql(rate)
				principal_amt = int(pb_item[5])
				due_days = (date.today() - datetime.strptime(pb_item[1],"%Y-%M-%d").date()).days
				surcharge = int(pb_item[6]) + surcharge_calculator(principal_amt, rate, due_days)
				other_charges = int(pb_item[7])
				charge_list = {'Surcharge':surcharge, 'Other':other_charges, 'Principal':principal_amt}

				print('New Payment Entry')
				print('Initial Charges', charge_list)
		except StopIteration:
			break

		try:
			if fund == 0:
				rf_item = next(released_funds_iter)
				fund = int(rf_item[1])
				
				print('Fund Used Details', rf_item)
		except StopIteration:
			break

		fund = surcharge_subtract(charge_list, fund)
		print(pb_item[0])
		print(datetime.strptime(pb_item[0],"%Y-%M-%d").date())
		payments_arr = [pb_item[0], pb_item[1], pb_item[2], pb_item[3], charge_list['Principal'], charge_list['Surcharge'], charge_list['Other'], fund, current_date, rf_item[2], pb_item[4]]
		print(payments_arr)
		insert_data(database_file, 'Payments', payments_format, payments_arr)
		print('Final Charges', charge_list)
		print("Fund Left", fund)
		print()

	
	print()
	print()
	exit_menu = input("Press Any Key To Continue...")

def modify_bill_type_details():
	cls_screen()
	print("=============================================================")
	print("                  Modify Bill Type Details")
	print("=============================================================")
	print()
	
	print()
	print()
	exit_menu = input("Press Any Key To Continue...")

def add_bill_type_details():
	cls_screen()
	print("=============================================================")
	print("                   Add Bill Type Details")
	print("=============================================================")
	print()
	i_b_type = input("\tEnter Bill Type:   ")
	i_days = int(input("\tEnter Due Interval:   "))
	i_rate = float(input("\tEnter Rate for Surcharge:    "))
	try:
		insert_data(database_file, 'Bill_Type', bill_type_format, [i_b_type, i_days, i_rate])
	except sqlite3.IntegrityError:
		print("Error")
	print()
	print()
	exit_menu = input("Press Any Key To Continue...")

def display_bill_type_details():
	cls_screen()
	print("=============================================================")
	print("                  Display Bill Type Details")
	print("=============================================================")
	print()
	val = retrieve_table(database_file, 'Bill_Type', '*', '')
	print(val)
	print()
	print()
	exit_menu = input("Press Any Key To Continue...")

def show_payment_bill_table():
	cls_screen()
	print("=============================================================")
	print("                     Payment Bill Table")
	print("=============================================================")
	print()
	val = retrieve_table(database_file, 'Payment_Bills', '*', '')
	for i in val:
		print(i)
	print()
	print()
	exit_menu = input("Press Any Key To Continue...")	

def show_released_funds_table():
	cls_screen()
	print("=============================================================")
	print("                     Released Funds Table")
	print("=============================================================")
	print()
	val = retrieve_table(database_file, 'Released_Funds', '*', '')
	for i in val:
		print(i)
	print()
	print()
	exit_menu = input("Press Any Key To Continue...")	
	pass


def test_func():
	cls_screen()
	t_data = ['2018-11-23', '2018-12-30', 'D', '300011', '2019-02-11::06:13:44:981574', '3000', '0', '0']
	update_table(database_file, 'Payment_Bills', payment_bill_format, t_data, 'pb_transaction_id', '2019-02-11::06:13:44:981574')

	print()
	print()
	exit_menu = input("Press Any Key To Continue...")

def ammendments():
	cls_screen()
	print("=============================================================")
	print("                     Ammendments")
	print("=============================================================")
	print()
	value = retrieve_table(database_file, 'Payments', '*', '')
	for i in value:
		print(i)

	print()
	print()
	exit_menu = input("Press Any Key To Continue...")


















