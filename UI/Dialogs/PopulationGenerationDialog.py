from PyQt5.QtWidgets import QDialog

from UI.Layouts.PopulationGenerationDialog import Ui_PopulationGenerationDialog

class PopulationGenerationDialog(QDialog):

    def __init__(self, parent = None):
        QDialog.__init__(self, parent)
        self.ui = Ui_PopulationGenerationDialog()
        self.ui.setupUi(self)

    def getUnitCount(self):
        return self.ui.spinBoxUnitCount.value()

    def getMethod(self):
        method = self.ui.comboBoxMethod.currentText()
        if method == "Random (recommended)":
            return "rand"
        elif method == "Depth search":
            return "ds"
        else:
            return None

    @staticmethod
    def getPopulationGenerationProperties(parent = None):
        populationDialog = PopulationGenerationDialog(parent)
        accepted = populationDialog.exec_()
        if accepted == QDialog.Rejected:
            return (None, None, False)
        unitCount = populationDialog.getUnitCount()
        method = populationDialog.getMethod()
        return (unitCount, method, True)
