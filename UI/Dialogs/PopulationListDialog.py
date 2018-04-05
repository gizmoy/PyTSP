from PyQt5.QtWidgets import QDialog, QTableWidgetItem

from UI.Layouts.PopulationListDialog import Ui_PopulationListDialog

class PopulationListDialog(QDialog):
	def __init__(self, parent = None, population = None):
		QDialog.__init__(self, parent)
		self.ui = Ui_PopulationListDialog()
		self.ui.setupUi(self)
		if population is None:
			return
		self.ui.tableWidget.setRowCount(population.size)
		for i in range(len(population.units)):
			unit = population.units[i]
			unitFitnessItem = QTableWidgetItem(str(unit.fitness))
			unitPathStr = ""
			for j in range(len(unit.path)):
				if j != 0:
					unitPathStr += "-"
				unitPathStr += str(unit.path[j])

			unitPathItem = QTableWidgetItem(unitPathStr)
			self.ui.tableWidget.setItem(i, 0, unitFitnessItem)
			self.ui.tableWidget.setItem(i, 1, unitPathItem)
