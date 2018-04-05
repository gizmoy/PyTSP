from PyQt5.QtWidgets import QDialog

from UI.Layouts.EvolutionParametersDialog import Ui_EvolutionParametersDialog

class EvolutionParametersDialog(QDialog):

    def __init__(self, parent = None):
        QDialog.__init__(self, parent)
        self.ui = Ui_EvolutionParametersDialog()
        self.ui.setupUi(self)

    def getParentCount(self):
        return self.ui.spinBoxParentCount.value()

    def getDepthSearch(self):
        return bool(self.ui.radioButtonDepthSearchYes.isChecked())

    def getMutationMethod(self):
        return self.ui.comboBoxMutator.currentText()

    def getProbability(self):
        return (self.ui.spinBoxProbability.value() / 100)

    def getElitismFactor(self):
        return self.ui.spinBoxElitism.value()

    def getTournamentSize(self):
        return self.ui.spinBoxTournamentSize.value()

    @staticmethod
    def getEvolutionParameters(parent = None):
        evolutionParametersDialog = EvolutionParametersDialog(parent)
        accepted = evolutionParametersDialog.exec_()
        if accepted == QDialog.Rejected:
            return (None, None, None, None, None, False)

        parentCount = evolutionParametersDialog.getParentCount()
        depthSearch = evolutionParametersDialog.getDepthSearch()
        mutationMethod = evolutionParametersDialog.getMutationMethod()
        probability = evolutionParametersDialog.getProbability()
        elitismFactor = evolutionParametersDialog.getElitismFactor()
        tournamentSize = evolutionParametersDialog.getTournamentSize()

        return (parentCount, depthSearch, mutationMethod, probability, elitismFactor, tournamentSize, True)
