from PyQt5.QtCore import QThread, pyqtSignal

from Map import Map

class MapGenerator(QThread):
    mapGenerated = pyqtSignal(Map)
    mapGenerationFailed = pyqtSignal(Exception)

    def __init__(self, parent = None):
        QThread.__init__(self, parent)
        self.fileMode = False
        self.fileName = ""
        self.citiesCount = 0
        self.connectionsCount = 0

    def setGenerationMode(self, fileMode = False, fileName = "", citiesCount = 0, connectionsCount = 0):
        self.fileMode = fileMode
        self.fileName = fileName
        self.citiesCount = citiesCount
        self.connectionsCount = connectionsCount

    def run(self):
        newMap = None
        if self.fileName:
            try:
                newMap = Map.readFromFile(self.fileName)
            except Exception as e:
                self.mapGenerationFailed.emit(e)
                return
        else:
            try:
                newMap = Map.generateCNN(self.citiesCount, self.connectionsCount)
            except Exception as e:
                self.mapGenerationFailed.emit(e)
                return

        self.mapGenerated.emit(newMap)
