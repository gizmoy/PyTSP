# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TSPGenMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TSPGenMainWindow(object):
	def setupUi(self, TSPGenMainWindow):
		TSPGenMainWindow.setObjectName("TSPGenMainWindow")
		TSPGenMainWindow.resize(600, 480)
		TSPGenMainWindow.setStatusTip("")
		self.centralwidget = QtWidgets.QWidget(TSPGenMainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
		self.verticalLayout.setObjectName("verticalLayout")
		self.graphicsViewMap = QtWidgets.QGraphicsView(self.centralwidget)
		self.graphicsViewMap.setObjectName("graphicsViewMap")
		self.verticalLayout.addWidget(self.graphicsViewMap)
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.checkBoxDisplayCities = QtWidgets.QCheckBox(self.centralwidget)
		self.checkBoxDisplayCities.setChecked(True)
		self.checkBoxDisplayCities.setObjectName("checkBoxDisplayCities")
		self.horizontalLayout.addWidget(self.checkBoxDisplayCities)
		self.checkBoxDisplayConnections = QtWidgets.QCheckBox(self.centralwidget)
		self.checkBoxDisplayConnections.setObjectName("checkBoxDisplayConnections")
		self.horizontalLayout.addWidget(self.checkBoxDisplayConnections)
		self.checkBoxDisplayBestUnit = QtWidgets.QCheckBox(self.centralwidget)
		self.checkBoxDisplayBestUnit.setChecked(True)
		self.checkBoxDisplayBestUnit.setObjectName("checkBoxDisplayBestUnit")
		self.horizontalLayout.addWidget(self.checkBoxDisplayBestUnit)
		self.verticalLayout.addLayout(self.horizontalLayout)
		TSPGenMainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(TSPGenMainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
		self.menubar.setObjectName("menubar")
		self.menuMap = QtWidgets.QMenu(self.menubar)
		self.menuMap.setObjectName("menuMap")
		self.menuPopulation = QtWidgets.QMenu(self.menubar)
		self.menuPopulation.setObjectName("menuPopulation")
		self.menuEvolution = QtWidgets.QMenu(self.menubar)
		self.menuEvolution.setObjectName("menuEvolution")
		TSPGenMainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(TSPGenMainWindow)
		self.statusbar.setSizeGripEnabled(True)
		self.statusbar.setObjectName("statusbar")
		TSPGenMainWindow.setStatusBar(self.statusbar)
		self.actionImportMap = QtWidgets.QAction(TSPGenMainWindow)
		self.actionImportMap.setObjectName("actionImportMap")
		self.actionGenerateMap = QtWidgets.QAction(TSPGenMainWindow)
		self.actionGenerateMap.setObjectName("actionGenerateMap")
		self.actionGeneratePopulation = QtWidgets.QAction(TSPGenMainWindow)
		self.actionGeneratePopulation.setObjectName("actionGeneratePopulation")
		self.actionDisplayPopulation = QtWidgets.QAction(TSPGenMainWindow)
		self.actionDisplayPopulation.setObjectName("actionDisplayPopulation")
		self.actionProcessGeneration = QtWidgets.QAction(TSPGenMainWindow)
		self.actionProcessGeneration.setObjectName("actionProcessGeneration")
		self.actionSetParameters = QtWidgets.QAction(TSPGenMainWindow)
		self.actionSetParameters.setObjectName("actionSetParameters")
		self.menuMap.addAction(self.actionImportMap)
		self.menuMap.addAction(self.actionGenerateMap)
		self.menuPopulation.addAction(self.actionGeneratePopulation)
		self.menuPopulation.addAction(self.actionDisplayPopulation)
		self.menuEvolution.addAction(self.actionSetParameters)
		self.menuEvolution.addAction(self.actionProcessGeneration)
		self.menubar.addAction(self.menuMap.menuAction())
		self.menubar.addAction(self.menuPopulation.menuAction())
		self.menubar.addAction(self.menuEvolution.menuAction())

		self.retranslateUi(TSPGenMainWindow)
		QtCore.QMetaObject.connectSlotsByName(TSPGenMainWindow)

	def retranslateUi(self, TSPGenMainWindow):
		_translate = QtCore.QCoreApplication.translate
		TSPGenMainWindow.setWindowTitle(_translate("TSPGenMainWindow", "TSPGen"))
		self.checkBoxDisplayCities.setText(_translate("TSPGenMainWindow", "Display cities"))
		self.checkBoxDisplayConnections.setText(_translate("TSPGenMainWindow", "Display connections"))
		self.checkBoxDisplayBestUnit.setText(_translate("TSPGenMainWindow", "Display best unit"))
		self.menuMap.setTitle(_translate("TSPGenMainWindow", "Map"))
		self.menuPopulation.setTitle(_translate("TSPGenMainWindow", "Population"))
		self.menuEvolution.setTitle(_translate("TSPGenMainWindow", "Evolution"))
		self.actionImportMap.setText(_translate("TSPGenMainWindow", "Import..."))
		self.actionGenerateMap.setText(_translate("TSPGenMainWindow", "Generate"))
		self.actionGeneratePopulation.setText(_translate("TSPGenMainWindow", "Generate new..."))
		self.actionDisplayPopulation.setText(_translate("TSPGenMainWindow", "Display"))
		self.actionProcessGeneration.setText(_translate("TSPGenMainWindow", "Process generation"))
		self.actionProcessGeneration.setShortcut(_translate("TSPGenMainWindow", "F9"))
		self.actionSetParameters.setText(_translate("TSPGenMainWindow", "Set parameters..."))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	TSPGenMainWindow = QtWidgets.QMainWindow()
	ui = Ui_TSPGenMainWindow()
	ui.setupUi(TSPGenMainWindow)
	TSPGenMainWindow.show()
	sys.exit(app.exec_())

