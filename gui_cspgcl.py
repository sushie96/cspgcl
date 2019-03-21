from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

from datetime import date
from datetime import timedelta


class cspgcl_main_page(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.setGeometry(50,50,700,400)
		self.setWindowTitle("CSPGCL")
		self.show()

		