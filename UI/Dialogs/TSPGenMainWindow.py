from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QLabel, QGraphicsScene

from UI import MapPainter
from UI.Dialogs import EvolutionParametersDialog, MapGenerationDialog, PopulationGenerationDialog, PopulationListDialog
from UI.Layouts.TSPGenMainWindow import Ui_TSPGenMainWindow
from UI.Wrappers import EvolutionProcessor, MapGenerator, PopulationGenerator

class TSPGenMainWindow(QMainWindow):
    """Docstring for TSPGenMainWindow"""

    def __init__(self):
        QMainWindow.__init__(self)
        self.problemMap = None
        self.population = None
        self.generation = 0

        self.statusbarMapMessage = "No problem map"
        self.statusbarPopulationMessage = "No population"
        self.statusbarBestUnitMessage = "No best unit"

        # Setup UI elements
        self.ui = Ui_TSPGenMainWindow()
        self.ui.setupUi(self)
        self.ui.statusbarLabel = QLabel("", self)
        self.ui.statusbarLabel.setObjectName("statusbarLabel")
        self.ui.statusbar.addPermanentWidget(self.ui.statusbarLabel)

        # Setup asynchronous objects
        self.mapGenerator = MapGenerator(self)
        self.evolutionProcessor = EvolutionProcessor(self)
        self.populationGenerator = PopulationGenerator(self)

        # Map painter
        displayCities = self.ui.checkBoxDisplayCities.isChecked()
        displayConnections = self.ui.checkBoxDisplayConnections.isChecked()
        displayBestUnit = self.ui.checkBoxDisplayBestUnit.isChecked()
        self.mapPainter = MapPainter(self, self.ui.graphicsViewMap, displayCities, displayConnections, displayBestUnit)

        # Refresh display elements
        self.refreshStatusbarMessage()

        # Setup UI actions - signals/slots
        self.setupUIActions()

    def setupUIActions(self):
        # Menu
        self.ui.actionImportMap.triggered.connect(self.importMap)
        self.ui.actionGenerateMap.triggered.connect(self.displayMapGenerationDialog)
        self.ui.actionGeneratePopulation.triggered.connect(self.displayPopulationGenerationDialog)
        self.ui.actionDisplayPopulation.triggered.connect(self.displayPopulationList)
        self.ui.actionSetParameters.triggered.connect(self.displayEvolutionParametersDialog)
        self.ui.actionProcessGeneration.triggered.connect(self.processGeneration)
        
        # Checkboxes
        self.ui.checkBoxDisplayCities.stateChanged.connect(self.toggleDisplayCities)
        self.ui.checkBoxDisplayConnections.stateChanged.connect(self.toggleDisplayConnections)
        self.ui.checkBoxDisplayBestUnit.stateChanged.connect(self.toggleDisplayBestUnit)

        # Async workers
        self.mapGenerator.mapGenerated.connect(self.mapGenerated)
        self.mapGenerator.mapGenerationFailed.connect(self.mapGenerationFailed)
        self.evolutionProcessor.generationProcessed.connect(self.generationProcessed)
        self.evolutionProcessor.generationProcessingFailed.connect(self.generationProcessingFailed)
        self.populationGenerator.populationGenerated.connect(self.populationGenerated)
        self.populationGenerator.populationGenerationFailed.connect(self.populationGenerationFailed)

        # Map View
        # self.ui.graphicsViewMap.rubberBandChanged.connect(self.mapPainter.repaint)

    def displayMapGenerationDialog(self):
        citiesCount, connectionsCount, statusOK = MapGenerationDialog.getMapProperties(self)
        if not statusOK:
            return
        self.mapGenerator.setGenerationMode(False, "", citiesCount, connectionsCount)
        self.statusbarMapMessage = "Loading problem map..."
        self.refreshStatusbarMessage()
        self.mapGenerator.start()

    def importMap(self):
        filename = QFileDialog.getOpenFileName(self, "TSPGen - load problem map", filter = "JSON File (*.json)")
        if not filename[0]:
            return

        self.mapGenerator.setGenerationMode(True, filename[0])
        self.statusbarMapMessage = "Loading problem map..."
        self.refreshStatusbarMessage()
        self.mapGenerator.start()

    def displayPopulationGenerationDialog(self):
        populationSize, method, statusOK = PopulationGenerationDialog.getPopulationGenerationProperties(self)
        if not statusOK:
            return
        self.populationGenerator.setGenerationParameters(self.problemMap, populationSize, method)
        self.statusbarPopulationMessage = "Generating population..."
        self.refreshStatusbarMessage()
        self.populationGenerator.start()

    def displayPopulationList(self):
        populationListDialog = PopulationListDialog(self, self.population)
        populationListDialog.exec_()

    def displayEvolutionParametersDialog(self):
        parentCount, depthSearch, mutationMethod, probability, elitismFactor, tournamentSize, statusOK = EvolutionParametersDialog.getEvolutionParameters(self)
        if not statusOK:
            return
        self.evolutionProcessor.setCrosserParameters(parentCount, depthSearch)
        self.evolutionProcessor.setMutatorParameters(mutationMethod, probability)
        self.evolutionProcessor.setSelectorParameters(tournamentSize, elitismFactor)

    def processGeneration(self):
        if self.problemMap is None:
            QMessageBox.warning(self, "TSPGen - Warning", "Cannot process generation - no problem map.", QMessageBox.Ok, QMessageBox.Ok)
            return
        if self.population is None:
            QMessageBox.warning(self, "TSPGen - Warning", "Cannot process generation - no population.", QMessageBox.Ok, QMessageBox.Ok)
            return
        self.evolutionProcessor.setProblemMap(self.problemMap)
        self.evolutionProcessor.setPopulation(self.population)
        self.statusbarPopulationMessage = "Processing generation..."
        self.refreshStatusbarMessage()
        self.evolutionProcessor.start()

    def toggleDisplayCities(self, state):
        self.mapPainter.setDisplayCities(state)
        self.mapPainter.repaint()

    def toggleDisplayConnections(self, state):
        self.mapPainter.setDisplayConnections(state)
        self.mapPainter.repaint()

    def toggleDisplayBestUnit(self, state):
        self.mapPainter.setDisplayBestUnit(state)
        self.mapPainter.repaint()

    def mapGenerated(self, problemMap):
        self.problemMap = problemMap
        self.statusbarMapMessage = "Map: {0} cities".format(problemMap.size)
        self.refreshStatusbarMessage()
        self.mapPainter.setProblemMap(problemMap)
        self.mapPainter.repaint()

    def mapGenerationFailed(self, e):
        QMessageBox.critical(self, "TSPGen - Error", "Error during map generation: {0}".format(e), QMessageBox.Ok, QMessageBox.Ok)
        self.statusbarMapMessage = "Map generation/loading failed"
        self.refreshStatusbarMessage()

    def generationProcessed(self, population):
        self.population = population
        self.generation += 1
        avgFitness = 0
        for u in population.units:
            avgFitness += u.fitness
        avgFitness = avgFitness / population.size
        self.statusbarPopulationMessage = "Generation: {0}, Avg fitness: {1}".format(self.generation, avgFitness)

        bestUnit = population.bestUnit()
        self.statusbarBestUnitMessage = "Best: {0}".format(bestUnit.fitness)
        self.refreshStatusbarMessage()

        self.mapPainter.setBestUnit(bestUnit)
        self.mapPainter.repaint()

    def generationProcessingFailed(self, e):
        QMessageBox.critical(self, "TSPGen - Error", "Error during generation processing: {0}".format(e), QMessageBox.Ok, QMessageBox.Ok)
        self.statusbarPopulationMessage = "Generation processing failed"
        self.refreshStatusbarMessage()

    def populationGenerated(self, population):
        self.population = population
        self.generation = 0
        avgFitness = 0
        for u in population.units:
            avgFitness += u.fitness
        avgFitness = avgFitness / population.size
        self.statusbarPopulationMessage = "Generation: {0}, Avg fitness: {1}".format(self.generation, avgFitness)

        bestUnit = population.bestUnit()
        self.statusbarBestUnitMessage = "Best: {0}".format(bestUnit.fitness)
        self.refreshStatusbarMessage()

        self.mapPainter.setBestUnit(bestUnit)
        self.mapPainter.repaint()

    def populationGenerationFailed(self, e):
        QMessageBox.critical(self, "TSPGen - Error", "Error during population generation: {0}".format(e), QMessageBox.Ok, QMessageBox.Ok)
        self.statusbarPopulationMessage = "Population generating failed"
        self.refreshStatusbarMessage()

    def refreshStatusbarMessage(self):
        self.ui.statusbarLabel.setText("{0} | {1} | {2}".format(self.statusbarMapMessage, self.statusbarPopulationMessage, self.statusbarBestUnitMessage))
