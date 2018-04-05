from PyQt5.QtWidgets import QDialog

from UI.Layouts.MapGenerationDialog import Ui_MapGenerationDialog

class MapGenerationDialog(QDialog):

	def __init__(self, parent = None):
		QDialog.__init__(self, parent)
		self.ui = Ui_MapGenerationDialog()
		self.ui.setupUi(self)
		self.setupUIActions()

	def setupUIActions(self):
		self.ui.spinBoxCities.valueChanged.connect(self.setMaxConnections)

	def setMaxConnections(self, citiesCount):
		self.ui.spinBoxConnections.setMaximum(citiesCount-1)

	def getCitiesCount(self):
		return self.ui.spinBoxCities.value()

	def getConnectionsCount(self):
		return self.ui.spinBoxConnections.value()

	@staticmethod
	def getMapProperties(parent = None):
		mapDialog = MapGenerationDialog(parent)
		accepted = mapDialog.exec_()
		if accepted == QDialog.Rejected:
			return (None, None, False)
		citiesCount = mapDialog.getCitiesCount()
		connectionsCount = mapDialog.getConnectionsCount()
		return (citiesCount, connectionsCount, True)
