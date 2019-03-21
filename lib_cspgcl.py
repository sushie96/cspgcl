import os
import sys

def cls_screen():
	if(sys.platform == 'linux'):
		os.system('cls')
	else:
		os.system('clear')

def exit_program():
	sys.exit()
	
def surcharge_subtract(charge_list, fund):
	for key, value in charge_list.items():
		if(fund - value) < 0:
			value = value - fund
			fund = 0
		else:
			fund = fund - value
			value = 0
		charge_list.update({key: value})
	return fund


def surcharge_calculator(amount, rate, days):
	return amount*rate*days

def extract_data_from_sql(data_list_all):
	data_tuple = data_list_all[0]
	data_list = list(data_tuple)
	data = data_list[0]
	return data




