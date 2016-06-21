from PyQt4 import QtGui, QtCore

class QEditButton(QtGui.QPushButton):
    def __init__(self, parent=None):
        super(QEditButton, self).__init__(parent)

    def switchBGColor(self, y):
        if y:
            self.setStyleSheet("background-color: rgb(153, 153, 255)")
        else:
            self.setStyleSheet("")
