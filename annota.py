# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'annota.ui'
#
# Created: Sat Mar 12 20:31:33 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Annota(object):
    def setupUi(self, Annota):
        Annota.setObjectName(_fromUtf8("Annota"))
        Annota.resize(1205, 807)
        self.prePanel = QtGui.QWidget(Annota)
        self.prePanel.setObjectName(_fromUtf8("prePanel"))
        self.gridLayout = QtGui.QGridLayout(self.prePanel)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.playerLayout = QtGui.QVBoxLayout()
        self.playerLayout.setObjectName(_fromUtf8("playerLayout"))
        self.frmInfoLabel = QtGui.QLabel(self.prePanel)
        self.frmInfoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.frmInfoLabel.setObjectName(_fromUtf8("frmInfoLabel"))
        self.playerLayout.addWidget(self.frmInfoLabel)
        self.frameView = QFrameView(self.prePanel)
        self.frameView.setMinimumSize(QtCore.QSize(800, 600))
        self.frameView.setMaximumSize(QtCore.QSize(1920, 1080))
        self.frameView.setObjectName(_fromUtf8("frameView"))
        self.playerLayout.addWidget(self.frameView)
        self.progSlider = QtGui.QSlider(self.prePanel)
        self.progSlider.setOrientation(QtCore.Qt.Horizontal)
        self.progSlider.setObjectName(_fromUtf8("progSlider"))
        self.playerLayout.addWidget(self.progSlider)
        self.playerControlLayout = QtGui.QHBoxLayout()
        self.playerControlLayout.setObjectName(_fromUtf8("playerControlLayout"))
        self.prevButton = QtGui.QPushButton(self.prePanel)
        self.prevButton.setObjectName(_fromUtf8("prevButton"))
        self.playerControlLayout.addWidget(self.prevButton)
        self.playButton = QtGui.QPushButton(self.prePanel)
        self.playButton.setObjectName(_fromUtf8("playButton"))
        self.playerControlLayout.addWidget(self.playButton)
        self.nextButton = QtGui.QPushButton(self.prePanel)
        self.nextButton.setObjectName(_fromUtf8("nextButton"))
        self.playerControlLayout.addWidget(self.nextButton)
        self.playerLayout.addLayout(self.playerControlLayout)
        self.gridLayout.addLayout(self.playerLayout, 0, 1, 1, 1)
        self.taskConfigLayout = QtGui.QFormLayout()
        self.taskConfigLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.taskConfigLayout.setObjectName(_fromUtf8("taskConfigLayout"))
        self.srcTypeBox = QtGui.QComboBox(self.prePanel)
        self.srcTypeBox.setObjectName(_fromUtf8("srcTypeBox"))
        self.srcTypeBox.addItem(_fromUtf8(""))
        self.srcTypeBox.addItem(_fromUtf8(""))
        self.srcTypeBox.addItem(_fromUtf8(""))
        self.srcTypeBox.addItem(_fromUtf8(""))
        self.taskConfigLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.srcTypeBox)
        self.olsBtnLayout = QtGui.QHBoxLayout()
        self.olsBtnLayout.setObjectName(_fromUtf8("olsBtnLayout"))
        self.openButton = QtGui.QPushButton(self.prePanel)
        self.openButton.setMaximumSize(QtCore.QSize(60, 16777215))
        self.openButton.setObjectName(_fromUtf8("openButton"))
        self.olsBtnLayout.addWidget(self.openButton)
        self.loadLabelButton = QtGui.QPushButton(self.prePanel)
        self.loadLabelButton.setMaximumSize(QtCore.QSize(90, 16777215))
        self.loadLabelButton.setObjectName(_fromUtf8("loadLabelButton"))
        self.olsBtnLayout.addWidget(self.loadLabelButton)
        self.saveLabelButton = QtGui.QPushButton(self.prePanel)
        self.saveLabelButton.setMaximumSize(QtCore.QSize(90, 16777215))
        self.saveLabelButton.setObjectName(_fromUtf8("saveLabelButton"))
        self.olsBtnLayout.addWidget(self.saveLabelButton)
        self.taskConfigLayout.setLayout(0, QtGui.QFormLayout.FieldRole, self.olsBtnLayout)
        self.tasksBox = QtGui.QComboBox(self.prePanel)
        self.tasksBox.setObjectName(_fromUtf8("tasksBox"))
        self.taskConfigLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.tasksBox)
        self.colorMapTabel = QtGui.QTableWidget(self.prePanel)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorMapTabel.sizePolicy().hasHeightForWidth())
        self.colorMapTabel.setSizePolicy(sizePolicy)
        self.colorMapTabel.setMinimumSize(QtCore.QSize(120, 0))
        self.colorMapTabel.setMaximumSize(QtCore.QSize(300, 16777215))
        self.colorMapTabel.setObjectName(_fromUtf8("colorMapTabel"))
        self.colorMapTabel.setColumnCount(3)
        self.colorMapTabel.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.colorMapTabel.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.colorMapTabel.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.colorMapTabel.setHorizontalHeaderItem(2, item)
        self.taskConfigLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.colorMapTabel)
        self.toolWidget = QtGui.QTabWidget(self.prePanel)
        self.toolWidget.setMinimumSize(QtCore.QSize(120, 200))
        self.toolWidget.setMaximumSize(QtCore.QSize(300, 16777215))
        self.toolWidget.setObjectName(_fromUtf8("toolWidget"))
        self.editTab = QtGui.QWidget()
        self.editTab.setEnabled(True)
        self.editTab.setObjectName(_fromUtf8("editTab"))
        self.line = QtGui.QFrame(self.editTab)
        self.line.setGeometry(QtCore.QRect(0, 130, 291, 16))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMinimumSize(QtCore.QSize(120, 0))
        self.line.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.layoutWidget = QtGui.QWidget(self.editTab)
        self.layoutWidget.setGeometry(QtCore.QRect(1, 2, 269, 29))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.editToolLayout = QtGui.QGridLayout(self.layoutWidget)
        self.editToolLayout.setMargin(0)
        self.editToolLayout.setObjectName(_fromUtf8("editToolLayout"))
        self.removeButton = QEditButton(self.layoutWidget)
        self.removeButton.setStyleSheet(_fromUtf8("QPushButton#removeButton:checked {\n"
"    background-color: rgb(0,255,0);\n"
"}"))
        self.removeButton.setCheckable(False)
        self.removeButton.setObjectName(_fromUtf8("removeButton"))
        self.editToolLayout.addWidget(self.removeButton, 0, 0, 1, 1)
        self.redoButton = QEditButton(self.layoutWidget)
        self.redoButton.setObjectName(_fromUtf8("redoButton"))
        self.editToolLayout.addWidget(self.redoButton, 0, 1, 1, 1)
        self.undoButton = QEditButton(self.layoutWidget)
        self.undoButton.setObjectName(_fromUtf8("undoButton"))
        self.editToolLayout.addWidget(self.undoButton, 0, 2, 1, 1)
        self.layoutWidget1 = QtGui.QWidget(self.editTab)
        self.layoutWidget1.setGeometry(QtCore.QRect(2, 140, 304, 24))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.annoCBox = QtGui.QCheckBox(self.layoutWidget1)
        self.annoCBox.setObjectName(_fromUtf8("annoCBox"))
        self.horizontalLayout.addWidget(self.annoCBox)
        self.prevCBox = QtGui.QCheckBox(self.layoutWidget1)
        self.prevCBox.setObjectName(_fromUtf8("prevCBox"))
        self.horizontalLayout.addWidget(self.prevCBox)
        self.autosaveCBox = QtGui.QCheckBox(self.layoutWidget1)
        self.autosaveCBox.setObjectName(_fromUtf8("autosaveCBox"))
        self.horizontalLayout.addWidget(self.autosaveCBox)
        self.toolWidget.addTab(self.editTab, _fromUtf8(""))
        self.tbcTab = QtGui.QWidget()
        self.tbcTab.setObjectName(_fromUtf8("tbcTab"))
        self.toolWidget.addTab(self.tbcTab, _fromUtf8(""))
        self.taskConfigLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.toolWidget)
        self.gridLayout.addLayout(self.taskConfigLayout, 0, 0, 1, 1)
        Annota.setCentralWidget(self.prePanel)
        self.statusbar = QtGui.QStatusBar(Annota)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Annota.setStatusBar(self.statusbar)

        self.retranslateUi(Annota)
        self.toolWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.prevButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Annota.prevFrame)
        QtCore.QObject.connect(self.nextButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Annota.nextFrame)
        QtCore.QObject.connect(self.frameView, QtCore.SIGNAL(_fromUtf8("sendSceneCoord(QString)")), self.statusbar.showMessage)
        QtCore.QObject.connect(self.progSlider, QtCore.SIGNAL(_fromUtf8("sliderReleased()")), Annota.toFrame)
        QtCore.QObject.connect(self.tasksBox, QtCore.SIGNAL(_fromUtf8("activated(QString)")), Annota.updateCMapBox)
        QtCore.QObject.connect(self.colorMapTabel, QtCore.SIGNAL(_fromUtf8("itemSelectionChanged()")), Annota.updatePenColor)
        QtCore.QObject.connect(self.frameView, QtCore.SIGNAL(_fromUtf8("hasSelectedItems(bool)")), self.removeButton.switchBGColor)
        QtCore.QObject.connect(self.removeButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.frameView.removeSelectedItems)
        QtCore.QObject.connect(self.redoButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.frameView.redo)
        QtCore.QObject.connect(self.undoButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.frameView.undo)
        QtCore.QObject.connect(self.frameView, QtCore.SIGNAL(_fromUtf8("reDoAble(bool)")), self.redoButton.switchBGColor)
        QtCore.QObject.connect(self.frameView, QtCore.SIGNAL(_fromUtf8("unDoAble(bool)")), self.undoButton.switchBGColor)
        QtCore.QObject.connect(self.openButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Annota.openSRCDialog)
        QtCore.QObject.connect(self.saveLabelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Annota.saveLabel)
        QtCore.QObject.connect(self.loadLabelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Annota.loadLabel)
        QtCore.QMetaObject.connectSlotsByName(Annota)

    def retranslateUi(self, Annota):
        Annota.setWindowTitle(_translate("Annota", "Annota", None))
        self.frmInfoLabel.setText(_translate("Annota", "TextLabel", None))
        self.prevButton.setText(_translate("Annota", "Prev", None))
        self.playButton.setText(_translate("Annota", "Play/Pause", None))
        self.nextButton.setText(_translate("Annota", "Next", None))
        self.srcTypeBox.setItemText(0, _translate("Annota", "Image", None))
        self.srcTypeBox.setItemText(1, _translate("Annota", "Image Folder", None))
        self.srcTypeBox.setItemText(2, _translate("Annota", "Video", None))
        self.srcTypeBox.setItemText(3, _translate("Annota", "Cam", None))
        self.openButton.setText(_translate("Annota", "Open", None))
        self.loadLabelButton.setText(_translate("Annota", "Load Label", None))
        self.saveLabelButton.setText(_translate("Annota", "Save Label", None))
        item = self.colorMapTabel.horizontalHeaderItem(0)
        item.setText(_translate("Annota", "ID", None))
        item = self.colorMapTabel.horizontalHeaderItem(1)
        item.setText(_translate("Annota", "COLOR", None))
        item = self.colorMapTabel.horizontalHeaderItem(2)
        item.setText(_translate("Annota", "LABEL", None))
        self.removeButton.setText(_translate("Annota", "REMOVE", None))
        self.redoButton.setText(_translate("Annota", "REDO", None))
        self.undoButton.setText(_translate("Annota", "UNDO", None))
        self.annoCBox.setText(_translate("Annota", "Annotation", None))
        self.prevCBox.setText(_translate("Annota", "Preview", None))
        self.autosaveCBox.setText(_translate("Annota", "Autosave", None))
        self.toolWidget.setTabText(self.toolWidget.indexOf(self.editTab), _translate("Annota", "Edit", None))
        self.toolWidget.setTabText(self.toolWidget.indexOf(self.tbcTab), _translate("Annota", "TBC", None))

from qframeview import QFrameView
from qeditbutton import QEditButton
