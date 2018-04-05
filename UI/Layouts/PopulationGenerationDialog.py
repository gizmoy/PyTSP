# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PopulationGenerationDialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PopulationGenerationDialog(object):
	def setupUi(self, PopulationGenerationDialog):
		PopulationGenerationDialog.setObjectName("PopulationGenerationDialog")
		PopulationGenerationDialog.resize(220, 110)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(PopulationGenerationDialog.sizePolicy().hasHeightForWidth())
		PopulationGenerationDialog.setSizePolicy(sizePolicy)
		PopulationGenerationDialog.setMinimumSize(QtCore.QSize(220, 110))
		PopulationGenerationDialog.setMaximumSize(QtCore.QSize(220, 110))
		self.verticalLayout = QtWidgets.QVBoxLayout(PopulationGenerationDialog)
		self.verticalLayout.setObjectName("verticalLayout")
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.labelUnitCount = QtWidgets.QLabel(PopulationGenerationDialog)
		self.labelUnitCount.setObjectName("labelUnitCount")
		self.horizontalLayout.addWidget(self.labelUnitCount)
		spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem)
		self.spinBoxUnitCount = QtWidgets.QSpinBox(PopulationGenerationDialog)
		self.spinBoxUnitCount.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
		self.spinBoxUnitCount.setMinimum(6)
		self.spinBoxUnitCount.setMaximum(50)
		self.spinBoxUnitCount.setProperty("value", 15)
		self.spinBoxUnitCount.setObjectName("spinBoxUnitCount")
		self.horizontalLayout.addWidget(self.spinBoxUnitCount)
		self.verticalLayout.addLayout(self.horizontalLayout)
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.labelMethod = QtWidgets.QLabel(PopulationGenerationDialog)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.labelMethod.sizePolicy().hasHeightForWidth())
		self.labelMethod.setSizePolicy(sizePolicy)
		self.labelMethod.setObjectName("labelMethod")
		self.horizontalLayout_2.addWidget(self.labelMethod)
		spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_2.addItem(spacerItem1)
		self.comboBoxMethod = QtWidgets.QComboBox(PopulationGenerationDialog)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.comboBoxMethod.sizePolicy().hasHeightForWidth())
		self.comboBoxMethod.setSizePolicy(sizePolicy)
		self.comboBoxMethod.setMinimumSize(QtCore.QSize(140, 20))
		self.comboBoxMethod.setMaximumSize(QtCore.QSize(140, 20))
		self.comboBoxMethod.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
		self.comboBoxMethod.setFrame(True)
		self.comboBoxMethod.setObjectName("comboBoxMethod")
		self.comboBoxMethod.addItem("")
		self.comboBoxMethod.addItem("")
		self.horizontalLayout_2.addWidget(self.comboBoxMethod)
		self.verticalLayout.addLayout(self.horizontalLayout_2)
		spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout.addItem(spacerItem2)
		self.buttonBox = QtWidgets.QDialogButtonBox(PopulationGenerationDialog)
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName("buttonBox")
		self.verticalLayout.addWidget(self.buttonBox)

		self.retranslateUi(PopulationGenerationDialog)
		self.buttonBox.accepted.connect(PopulationGenerationDialog.accept)
		self.buttonBox.rejected.connect(PopulationGenerationDialog.reject)
		QtCore.QMetaObject.connectSlotsByName(PopulationGenerationDialog)

	def retranslateUi(self, PopulationGenerationDialog):
		_translate = QtCore.QCoreApplication.translate
		PopulationGenerationDialog.setWindowTitle(_translate("PopulationGenerationDialog", "Population Generation"))
		self.labelUnitCount.setText(_translate("PopulationGenerationDialog", "Number of units"))
		self.labelMethod.setText(_translate("PopulationGenerationDialog", "Method"))
		self.comboBoxMethod.setItemText(0, _translate("PopulationGenerationDialog", "Random (recommended)"))
		self.comboBoxMethod.setItemText(1, _translate("PopulationGenerationDialog", "Depth search"))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	PopulationGenerationDialog = QtWidgets.QDialog()
	ui = Ui_PopulationGenerationDialog()
	ui.setupUi(PopulationGenerationDialog)
	PopulationGenerationDialog.show()
	sys.exit(app.exec_())

