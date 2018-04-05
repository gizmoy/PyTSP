# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MapGenerationDialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MapGenerationDialog(object):
	def setupUi(self, MapGenerationDialog):
		MapGenerationDialog.setObjectName("MapGenerationDialog")
		MapGenerationDialog.resize(200, 110)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(MapGenerationDialog.sizePolicy().hasHeightForWidth())
		MapGenerationDialog.setSizePolicy(sizePolicy)
		MapGenerationDialog.setMinimumSize(QtCore.QSize(200, 110))
		MapGenerationDialog.setMaximumSize(QtCore.QSize(200, 110))
		self.verticalLayout = QtWidgets.QVBoxLayout(MapGenerationDialog)
		self.verticalLayout.setObjectName("verticalLayout")
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.label = QtWidgets.QLabel(MapGenerationDialog)
		self.label.setObjectName("label")
		self.horizontalLayout.addWidget(self.label)
		spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem)
		self.spinBoxCities = QtWidgets.QSpinBox(MapGenerationDialog)
		self.spinBoxCities.setSpecialValueText("")
		self.spinBoxCities.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
		self.spinBoxCities.setMinimum(6)
		self.spinBoxCities.setProperty("value", 40)
		self.spinBoxCities.setObjectName("spinBoxCities")
		self.horizontalLayout.addWidget(self.spinBoxCities)
		self.verticalLayout.addLayout(self.horizontalLayout)
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.label_2 = QtWidgets.QLabel(MapGenerationDialog)
		self.label_2.setObjectName("label_2")
		self.horizontalLayout_2.addWidget(self.label_2)
		spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_2.addItem(spacerItem1)
		self.spinBoxConnections = QtWidgets.QSpinBox(MapGenerationDialog)
		self.spinBoxConnections.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
		self.spinBoxConnections.setMinimum(3)
		self.spinBoxConnections.setMaximum(39)
		self.spinBoxConnections.setProperty("value", 10)
		self.spinBoxConnections.setObjectName("spinBoxConnections")
		self.horizontalLayout_2.addWidget(self.spinBoxConnections)
		self.verticalLayout.addLayout(self.horizontalLayout_2)
		spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout.addItem(spacerItem2)
		self.buttonBox = QtWidgets.QDialogButtonBox(MapGenerationDialog)
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName("buttonBox")
		self.verticalLayout.addWidget(self.buttonBox)

		self.retranslateUi(MapGenerationDialog)
		self.buttonBox.accepted.connect(MapGenerationDialog.accept)
		self.buttonBox.rejected.connect(MapGenerationDialog.reject)
		QtCore.QMetaObject.connectSlotsByName(MapGenerationDialog)

	def retranslateUi(self, MapGenerationDialog):
		_translate = QtCore.QCoreApplication.translate
		MapGenerationDialog.setWindowTitle(_translate("MapGenerationDialog", "Map Generation"))
		self.label.setText(_translate("MapGenerationDialog", "Number of cities"))
		self.label_2.setText(_translate("MapGenerationDialog", "Number of connections"))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MapGenerationDialog = QtWidgets.QDialog()
	ui = Ui_MapGenerationDialog()
	ui.setupUi(MapGenerationDialog)
	MapGenerationDialog.show()
	sys.exit(app.exec_())

