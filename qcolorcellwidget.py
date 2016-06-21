#import sys
from PyQt4 import QtGui, QtCore

class QColorCellWidget(QtGui.QWidget):
    def __init__(self, pencolor, parent=None):
        super(QColorCellWidget, self).__init__(parent)
        self.pencolor = pencolor

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        pen = QtGui.QPen(QtGui.QColor(self.pencolor[0], self.pencolor[1], self.pencolor[2]), 4, QtCore.Qt.SolidLine) 
        qp.setPen(pen)
        qp.drawLine(10, 15, 45, 15)
        qp.end()

#if __name__ == '__main__':
#    app = QtGui.QApplication(sys.argv)
#    ex = QColorCellItem()
#    ex.show()
#    sys.exit(app.exec_())
