from PyQt4 import QtGui, QtCore
import sys

class QStrokeRect(QtGui.QGraphicsRectItem):
    def __init__(self, parent=None):
        super(QStrokeRect, self).__init__(parent)
        self.strokeWidth = 4
        self.setPen(QtGui.QPen(QtGui.QColor(255, 0, 0), 4, QtCore.Qt.SolidLine))
        self.setFlags(QtGui.QGraphicsItem.ItemIsSelectable)
        self.cateid = None

    def setStrokeWidth(self, strokeWidth):
        self.strokeWidth = strokeWidth

    def shape(self):
        path = QtGui.QPainterPath()
        path.addRect(self.boundingRect())
        pStroker = QtGui.QPainterPathStroker()
        pStroker.setWidth(self.strokeWidth)
        return pStroker.createStroke(path)

class QTestView(QtGui.QGraphicsView):
    def __init__(self, parent=None):
        super(QTestView, self).__init__(parent)
        self.scene = QtGui.QGraphicsScene(self)
        self.scene.setBackgroundBrush(QtGui.QBrush(QtCore.Qt.darkGray, QtCore.Qt.SolidPattern))
        self.setScene(self.scene)


class Example(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Example, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Select by stroke')
        self.gv = QTestView(self)
        self.gv.setMouseTracking(True)
        self.pen = QtGui.QPen(QtGui.QColor(255, 0, 0), 4, QtCore.Qt.SolidLine)
        self.gv.scene.addRect(QtCore.QRectF(0,0,400,400), self.pen)
        self.gv.scene.addItem(QStrokeRect(QtCore.QRectF(100,100,100,100)))
        self.gv.scene.addItem(QStrokeRect(QtCore.QRectF(150,150,100,100)))



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()

    
