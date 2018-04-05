# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PopulationListDialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PopulationListDialog(object):
	def setupUi(self, PopulationListDialog):
		PopulationListDialog.setObjectName("PopulationListDialog")
		PopulationListDialog.resize(423, 306)
		self.verticalLayout = QtWidgets.QVBoxLayout(PopulationListDialog)
		self.verticalLayout.setObjectName("verticalLayout")
		self.tableWidget = QtWidgets.QTableWidget(PopulationListDialog)
		self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
		self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
		self.tableWidget.setShowGrid(True)
		self.tableWidget.setGridStyle(QtCore.Qt.DashLine)
		self.tableWidget.setWordWrap(False)
		self.tableWidget.setColumnCount(2)
		self.tableWidget.setObjectName("tableWidget")
		self.tableWidget.setRowCount(0)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(0, item)
		item = QtWidgets.QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(1, item)
		self.tableWidget.horizontalHeader().setVisible(True)
		self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
		self.tableWidget.horizontalHeader().setDefaultSectionSize(70)
		self.tableWidget.horizontalHeader().setStretchLastSection(True)
		self.verticalLayout.addWidget(self.tableWidget)
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem)
		self.pushButtonClose = QtWidgets.QPushButton(PopulationListDialog)
		self.pushButtonClose.setDefault(True)
		self.pushButtonClose.setObjectName("pushButtonClose")
		self.horizontalLayout.addWidget(self.pushButtonClose)
		self.verticalLayout.addLayout(self.horizontalLayout)

		self.retranslateUi(PopulationListDialog)
		self.pushButtonClose.released.connect(PopulationListDialog.close)
		QtCore.QMetaObject.connectSlotsByName(PopulationListDialog)

	def retranslateUi(self, PopulationListDialog):
		_translate = QtCore.QCoreApplication.translate
		PopulationListDialog.setWindowTitle(_translate("PopulationListDialog", "Population List"))
		self.tableWidget.setSortingEnabled(False)
		item = self.tableWidget.horizontalHeaderItem(0)
		item.setText(_translate("PopulationListDialog", "Fitness"))
		item = self.tableWidget.horizontalHeaderItem(1)
		item.setText(_translate("PopulationListDialog", "Path"))
		self.pushButtonClose.setText(_translate("PopulationListDialog", "Close"))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	PopulationListDialog = QtWidgets.QDialog()
	ui = Ui_PopulationListDialog()
	ui.setupUi(PopulationListDialog)
	PopulationListDialog.show()
	sys.exit(app.exec_())

