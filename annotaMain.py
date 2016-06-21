from PyQt4 import QtGui, QtCore
from annota import Ui_Annota
from qcolorcellwidget import QColorCellWidget
from cmapgen import get_colors

import sys
import os
import numpy as np
import pandas as pd


class Annota(QtGui.QMainWindow, Ui_Annota):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.ith = None
        self.labels = pd.DataFrame(index=[], columns=['image', 'cateid', 'tlx', 'tly', 'width', 'height'])
        self.labelsBuf = pd.DataFrame(index=[], columns=['image', 'cateid', 'tlx', 'tly', 'width', 'height'])
        self.labelFile = ''
        self._penwidth = 2 # even value
        self._offset = self._penwidth/2
        self.initializeTasks()

    def initFrameView(self):
        self.ith = 0
        self.labels = pd.DataFrame(index=[], columns=['image', 'cateid', 'tlx', 'tly', 'width', 'height'])
        self.labelsBuf = pd.DataFrame(index=[], columns=['image', 'cateid', 'tlx', 'tly', 'width', 'height'])
        self.labelFile = ''
        self.num = len(self.imgsList)
        self.updateFrameView()

    def prevFrame(self):
        if self.ith is not None:
            if self.ith:
                self.updateLabelsBufOrSave()
                self.ith -= 1
                self.updateFrameView()

    def nextFrame(self):
        if self.ith is not None:
            if (self.num - 1 - self.ith):
                self.updateLabelsBufOrSave()
                self.ith += 1
                self.updateFrameView()

    def toFrame(self):
        if self.ith is not None:
            self.updateLabelsBufOrSave()
            self.ith = self.progSlider.value() * self.num / 100
            self.updateFrameView()


    def updateFrameView(self):
        imgPixmap = QtGui.QPixmap(self.imgsList[self.ith])
        self.frmInfoLabel.setText('{}/{} - {} ({}x{})'.format(self.ith+1, self.num, os.path.basename(self.imgsList[self.ith]), imgPixmap.width(), imgPixmap.height()))
        self.frameView.scene.clear()
        self.frameView.scene.setSceneRect(0,0,imgPixmap.width(),imgPixmap.height())
        imgItem = self.frameView.scene.addPixmap(imgPixmap)
        self.frameView.centerOn(imgItem)
        self.frameView.resetTransform()
        self.frameView.clearStack()
        self.progSlider.setValue((self.ith+1) * 100 / self.num)
        inbuf = self.labelsBuf[self.labelsBuf.image == os.path.basename(self.imgsList[self.ith])]
        if len(inbuf):
            self.frameView.setBaseRects(inbuf[inbuf.cateid.notnull()][['cateid','tlx','tly','width','height']].values)
            self.frameView.showBaseRects()
        else:
            inlabels = self.labels[self.labels.image == os.path.basename(self.imgsList[self.ith])]
            if len(inlabels):
                self.frameView.setBaseRects(inlabels[['cateid','tlx','tly','width','height']].values)
                self.frameView.showBaseRects()
            else:
                self.frameView.setBaseRects([])
        self.updateLabelsBuf()
 
    # TEARS:
    # need to update buf before leaving each image ***AND*** after loading marks for a new image 
    # that is not in buf yet. tricky case (after saving labels or right after 
    # loading a not yet in buf new image): suppose loading a new image with marks, 
    # and buf has no enteries about this new image, after deleting all the 
    # marks and go to next image, the deletion of all marks will not be recorded 
    # in buf, that's why also need to update buf after loading all marks for the 
    # new image which is not in buf yet. 
    
    def updateLabelsBuf(self):
        boxes = self.frameView.scene.items()[:-1]
        img = os.path.basename(self.imgsList[self.ith])
        boxesRows = []
        if len(boxes):
            boxesRows = [{'image':img, 'cateid':box.cateid, 'tlx':box.boundingRect().x()+self._offset, 'tly':box.boundingRect().y()+self._offset, 'width':box.boundingRect().width()-self._penwidth, 'height':box.boundingRect().height()-self._penwidth} for box in boxes]
        elif img in self.labelsBuf.image.values:
            boxesRows = [{'image':img}]
        self.labelsBuf = self.labelsBuf[self.labelsBuf.image != img]
        if len(boxesRows):
            self.labelsBuf = self.labelsBuf.append(boxesRows, ignore_index=True)
        #print self.labelsBuf
 
    def updateLabelsBufOrSave(self):
        if self.autosaveCBox.isChecked():
            self.saveLabel()
        else:
            self.updateLabelsBuf()

    def saveLabel(self):
        if not len(self.labelFile):
            self.labelFile = QtGui.QFileDialog.getSaveFileName(self, 'Save Label File', os.path.expanduser('~'), 'Txt (*.txt)')

        if len(self.labelFile):
            self.updateLabelsBuf()
            if self.labelsBuf is not None:
                if self.labels is None:
                    self.labels = self.labelsBuf
                
                self.labels = self.labels[~self.labels.image.isin(pd.unique(self.labelsBuf.image.ravel()))]
                self.labelsBuf = self.labelsBuf[self.labelsBuf.cateid.notnull()]
                self.labels = self.labels.append(self.labelsBuf, ignore_index=True)
                self.labels.to_csv(self.labelFile, index=False)
                self.labelsBuf = self.labelsBuf[self.labelsBuf.image == os.path.basename(self.imgsList[self.ith])]


    def loadLabel(self):
        self.labelFile = QtGui.QFileDialog.getOpenFileName(self, 'Choose Label File', os.path.expanduser('~'), 'Txt (*.txt)')
        if len(self.labelFile):
            self.labels = pd.read_csv(str(self.labelFile))
            self.updateLabelsBuf()
            self.updateFrameView()


    def openSRCDialog(self):
        if self.srcTypeBox.currentText() == 'Image':
            imgs = QtGui.QFileDialog.getOpenFileNames(self, 'Open Images', os.path.expanduser('~'), 'Images (*.png *.jpg *bmp)')
            if len(imgs):
                self.imgsList = map(str, imgs)
                self.imgsList.sort()
                self.initFrameView()
        elif self.srcTypeBox.currentText() == 'Image Folder':
            fdpth = str(QtGui.QFileDialog.getExistingDirectory(self, 'Open Directory', os.path.expanduser('~')))
            if len(fdpth):
                self.imgsList = [os.path.join(fdpth, img) for img in os.listdir(fdpth) if img.lower().endswith(('.png', '.jpg', '.bmp'))]
                self.imgsList.sort()
                self.initFrameView()
        else:
            pass


    def initializeTasks(self):
        self.colorMapTabel.setColumnWidth(0,40)
        self.colorMapTabel.setColumnWidth(1,60)
        self.colorMapTabel.horizontalHeader().setStretchLastSection(True)
        self.colorMapTabel.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.colorMapTabel.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self._parseConfig()
        for q_tname in sorted(self.tasks):
            self.tasksBox.addItem(q_tname)
        self.updateCMapBox(sorted(self.tasks)[0])

    def updateCMapBox(self, q_tname):
        self.colorMapTabel.clearContents()
        tname = str(q_tname)
        self.colorMapTabel.setRowCount(len(self.tasks[tname]))
        self.cmap = get_colors(len(self.tasks[tname]))  # 0-1 range
        self.frameView.cmap = self.cmap
        self.frameView.penwidth = self._penwidth

        for i in sorted(self.tasks[tname]):
            idx = QtGui.QTableWidgetItem(str(i))
            idx.setTextAlignment(QtCore.Qt.AlignCenter)
            idx.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.colorMapTabel.setItem(i, 0, idx)

            col = QColorCellWidget(tuple(int(255*c) for c in self.cmap[i]))
            self.colorMapTabel.setCellWidget(i, 1, col)

            lab = QtGui.QTableWidgetItem(self.tasks[tname][i])
            lab.setTextAlignment(QtCore.Qt.AlignCenter)
            lab.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.colorMapTabel.setItem(i, 2, lab)

    def updatePenColor(self):
        if len(self.colorMapTabel.selectionModel().selectedRows()):
            selIdx = self.colorMapTabel.selectionModel().selectedRows()[0].row()
            self.frameView.setPen(selIdx)
        else:
            self.frameView.setPen(None, None)


    def _parseConfig(self):
        self.tasks = {}
        with open('configs/tasks', 'r') as f:
            for l in f.readlines()[1:]:
                [tname, tlabels] = l.strip().split(',')
                tlabelsClean = [tl.strip() for tl in tlabels.strip().split(';')]
                self.tasks[tname] = dict(zip(range(len(tlabelsClean)), tlabelsClean))


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    annota = Annota()
    annota.show()
    app.exec_()
