from os import *
#import sys
from datetime import date
from datetime import timedelta

# from parameters import *
# from database import *
from lib_cspgcl import *
from main_cspgcl import *
#from gui_cspgcl import *

def main():
	create_table_main()

	while(1):
		cls_screen()
		print("=============================================================")
		print("                         Main Menu")
		print("=============================================================")
		print()
		print("\t1.  Enter Payment Bill Details")
		print("\t2.  Enter Released Fund Details")
		print("\t3.  Settle Bills")
		print("\t4.  Modify Bill Type Data")
		print("\t5.  Add New Bill Type Data")
		print("\t6.  Display Bill Type Data")
		print("\t7.  Show Payment Bill Table")
		print("\t8.  Show Released Funds Table new func")
		print("\t9.  Ammendments")
		print("\t0.  Exit Program")
		print()
		menu_option = input("\tSelect the desired option:   ")

		if(menu_option == '1'):
			payment_bill_details()
		elif(menu_option == '2'):
			released_fund_details()
		elif(menu_option == '3'):
			settle_bills(date.today())
		elif(menu_option == '4'):
			modify_bill_type_details()
		elif(menu_option == '5'):
			add_bill_type_details()
		elif(menu_option == '6'):
			display_bill_type_details()
		elif(menu_option == '7'):
			show_payment_bill_table()
		elif(menu_option == '8'):
			#show_released_funds_table()
			test_func()
		elif(menu_option == '9'):
			ammendments()
		elif(menu_option == '0'):
			exit_program()
		else:
			exit_program()

		

	
if __name__ == "__main__":
	main()