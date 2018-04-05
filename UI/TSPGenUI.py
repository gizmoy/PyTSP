import sys
from PyQt5.QtWidgets import QApplication

from UI.Dialogs import TSPGenMainWindow

class TSPGenUI(object):
	def __init__(self):
		pass

	def exec_(self):
		app = QApplication(sys.argv)
		program = TSPGenMainWindow()
		program.show()
		return app.exec_()
