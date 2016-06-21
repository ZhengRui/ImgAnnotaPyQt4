from PyQt4 import QtGui, QtCore
from qstrokerect import QStrokeRect

class QFrameView(QtGui.QGraphicsView):
    def __init__(self, parent=None):
        QtGui.QGraphicsView.__init__(self, parent)
        self.scene = QtGui.QGraphicsScene(self)
        self.scene.setBackgroundBrush(QtGui.QBrush(QtCore.Qt.darkGray, QtCore.Qt.SolidPattern))
        self.setScene(self.scene)

        self.setDragMode(QtGui.QGraphicsView.ScrollHandDrag)
        self.setTransformationAnchor(QtGui.QGraphicsView.AnchorUnderMouse)
        self.viewport().setCursor(QtCore.Qt.CrossCursor)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self._pan = False
        self._draw = False
        self._moved = False
        self._sel = False
        self.pen = None
        self.penid = None
        self.cmap = None
        self.penwidth = 4
        self._redoStack = []
        self._histStates = []
        self._baseRects = []

    def wheelEvent(self, event):
        zoomOFactor = 1.15
        zoomIFactor = 1.0 / zoomOFactor
        if event.delta() > 0:
            self.scale(zoomOFactor, zoomOFactor)
        else:
            self.scale(zoomIFactor, zoomIFactor)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.RightButton:
            self._pan = True
            self._panStartX = event.x()
            self._panStartY = event.y()
            self.viewport().setCursor(QtCore.Qt.ClosedHandCursor)
        else:
            # do image annotation 
            if self.scene.sceneRect().width() > 1e-3 and self.pen is not None and self.sceneRect().contains(self.mapToScene(event.pos())):
                if not self._sel:
                    self._draw = True
                    sceneCoord = self.mapToScene(event.pos())
                    self._drawStartX = sceneCoord.x()
                    self._drawStartY = sceneCoord.y()
                    self._lstRect = self.scene.addRect(self._drawStartX-2, self._drawStartY-2, 4, 4, self.pen)
                elif self.selItem is not None:
                    self.selItem.setSelected(True)
            else:
                self.scene.clearSelection()
        event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.RightButton:
            self._pan = False
            self.viewport().setCursor(QtCore.Qt.CrossCursor)
        else:
            if self._draw:
                self.scene.clearSelection()
                if not self._moved:
                    self.scene.removeItem(self._lstRect)
                else:
                    self._lstRect.setSelected(True)
                    self._lstRect.cateid = self.penid
                    self.snapShot()
                    self._redoStack = []

            self._draw = False
            self._moved = False

        self.emit(QtCore.SIGNAL("hasSelectedItems(bool)"), len(self.scene.selectedItems())>0)
        event.accept()

    def mouseMoveEvent(self, event):
        if self._pan:
            self.horizontalScrollBar().setValue(self.horizontalScrollBar().value() - (event.x() - self._panStartX))
            self.verticalScrollBar().setValue(self.verticalScrollBar().value() - (event.y() - self._panStartY))
            self._panStartX = event.x()
            self._panStartY = event.y()

        if self._draw:
            self.scene.removeItem(self._lstRect)
            sceneCoord = self.mapToScene(event.pos())
            tl = QtCore.QPointF(max(min(self._drawStartX, sceneCoord.x())-2, 0), max(min(self._drawStartY, sceneCoord.y())-2, 0))
            br = QtCore.QPointF(min(max(self._drawStartX, sceneCoord.x()-1)+2, self.scene.sceneRect().width()), min(max(self._drawStartY, sceneCoord.y()-1)+2, self.scene.sceneRect().height()))
            self._lstRect = QStrokeRect(QtCore.QRectF(tl, br))
            self._lstRect.setPen(self.pen)
            self._lstRect.setStrokeWidth(6)
            self.scene.addItem(self._lstRect)
            self._moved = True

        event.accept()
        QtGui.QGraphicsView.mouseMoveEvent(self, event)

        sceneCoord = self.mapToScene(event.pos())
        sceneRect = self.scene.sceneRect()
        if sceneRect.contains(sceneCoord):
            self.emit(QtCore.SIGNAL("sendSceneCoord(QString)"), QtCore.QString('{:04.2f}, {:04.2f}'.format(sceneCoord.x(), sceneCoord.y())))
            if not self._pan and not self._draw:
                self.selItem = self.scene.itemAt(sceneCoord)
                if self.selItem is not None and self.selItem.type() != 7:   # 7 is QGraphicsPixmapItem
                    self.viewport().setCursor(QtCore.Qt.ArrowCursor)
                    self._sel = True
                else:
                    self.viewport().setCursor(QtCore.Qt.CrossCursor)
                    self._sel = False
        else:
            self.emit(QtCore.SIGNAL("sendSceneCoord(QString)"), '')


    def setPen(self, penid):
        self.pen = QtGui.QPen(QtGui.QColor(int(255*self.cmap[penid][0]), int(255*self.cmap[penid][1]), int(255*self.cmap[penid][2])), self.penwidth, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin)
        self.penid = penid

    def removeSelectedItems(self):
        if len(self.scene.selectedItems()):
            for item in self.scene.selectedItems():
                self.scene.removeItem(item)
                item.setSelected(False)
            self.viewport().update()
            self.snapShot()
            self._redoStack = []
            self.emit(QtCore.SIGNAL("hasSelectedItems(bool)"), False)

    def undo(self):
        self.scene.clearSelection()
        self.emit(QtCore.SIGNAL("hasSelectedItems(bool)"), False)
        if len(self._histStates):
            self._redoStack.append(self._histStates.pop())
            self.updateFromHist()

    def redo(self):
        self.scene.clearSelection()
        self.emit(QtCore.SIGNAL("hasSelectedItems(bool)"), False)
        if len(self._redoStack):
            self._histStates.append(self._redoStack.pop())
            self.updateFromHist()

    def snapShot(self):
        self._histStates.append([item for item in self.scene.items()[:-1]])
        self.emit(QtCore.SIGNAL("reDoAble(bool)"), False)
        self.emit(QtCore.SIGNAL("unDoAble(bool)"), True)

    def updateFromHist(self):
        for item in self.scene.items()[:-1]:
            self.scene.removeItem(item)
        if len(self._histStates):
            for item in self._histStates[-1]:
                self.scene.addItem(item)
        else:
            self.showBaseRects()
        self.viewport().update()
        self.emit(QtCore.SIGNAL("reDoAble(bool)"), len(self._redoStack)>0)
        self.emit(QtCore.SIGNAL("unDoAble(bool)"), len(self._histStates)>0)

    def clearStack(self):
        self._histStates = []
        self._redoStack = []
        self.emit(QtCore.SIGNAL("reDoAble(bool)"), False)
        self.emit(QtCore.SIGNAL("unDoAble(bool)"), False)
        self.emit(QtCore.SIGNAL("hasSelectedItems(bool)"), False)

    def setBaseRects(self, rectArrs):
        self._baseRects = rectArrs        
    
    def showBaseRects(self):
        for rect in self._baseRects:
            self._lstRect = QStrokeRect(QtCore.QRectF(rect[1], rect[2], rect[3], rect[4]))
            cateid = int(rect[0])
            self._lstRect.setPen(QtGui.QPen(QtGui.QColor(int(255*self.cmap[cateid][0]), int(255*self.cmap[cateid][1]), int(255*self.cmap[cateid][2])), self.penwidth, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
            self._lstRect.cateid = cateid
            self._lstRect.setStrokeWidth(6)
            self.scene.addItem(self._lstRect)
