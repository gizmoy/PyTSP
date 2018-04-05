from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen, QBrush, QColor
from PyQt5.QtWidgets import QGraphicsScene

class MapPainter(object):
    def __init__(self, parent, view, displayCities, displayConnections, displayBestUnit):
        super().__init__()
        self.view = view
        self.displayCities = displayCities
        self.displayConnections = displayConnections
        self.displayBestUnit = displayBestUnit
        self.problemMap = None
        self.bestUnit = None

        self.scene = QGraphicsScene(parent)
        self.resizeScene()

        self.view.setScene(self.scene)
        self.view.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)

    def resizeScene(self):
        height = self.view.size().height()
        width = self.view.size().width()
        self.scene.setSceneRect(0.0, 0.0, width, height)

    def setProblemMap(self, problemMap):
        self.problemMap = problemMap

    def setBestUnit(self, unit):
        self.bestUnit = unit

    def setDisplayCities(self, enabled = False):
        self.displayCities = bool(enabled)

    def setDisplayConnections(self, enabled = False):
        self.displayConnections = bool(enabled)

    def setDisplayBestUnit(self, enabled = False):
        self.displayBestUnit = bool(enabled)

    def repaint(self):
        if self.problemMap is None:
            return

        self.scene.clear()
        self.resizeScene()
        height = self.scene.height()
        width = self.scene.width()

        if self.displayCities:
            cityBrush = QBrush(QColor(0, 0, 0), Qt.SolidPattern)
            cityPen = QPen(cityBrush, 5.0)
            for city in self.problemMap.cities:
                x = width * city.positionX
                y = height * city.positionY
                self.scene.addEllipse(x, y, 4, 4, cityPen, cityBrush)

        if self.displayConnections:
            connectionBrush = QBrush(QColor(0, 0, 255), Qt.SolidPattern)
            connectionPen = QPen(connectionBrush, 1.0)
            for city in self.problemMap.cities:
                for neighbour in city.connections:
                    x = width * city.positionX
                    y = height * city.positionY
                    x2 = width * self.problemMap.cities[neighbour].positionX
                    y2 = height * self.problemMap.cities[neighbour].positionY
                    self.scene.addLine(x, y, x2, y2, connectionPen)

        if self.displayBestUnit and self.bestUnit is not None:
            bestUnitBrush = QBrush(QColor(255, 0, 0), Qt.SolidPattern)
            bestUnitPen = QPen(bestUnitBrush, 2.0)
            for i in range(-1, len(self.bestUnit.path)-1):
                currCity = self.problemMap.cities[self.bestUnit.path[i]]
                nextCity = self.problemMap.cities[self.bestUnit.path[i+1]]
                x = width * currCity.positionX
                y = height * currCity.positionY
                x2 = width * nextCity.positionX
                y2 = height * nextCity.positionY
                self.scene.addLine(x, y, x2, y2, bestUnitPen)

        self.view.fitInView(self.scene.sceneRect())
