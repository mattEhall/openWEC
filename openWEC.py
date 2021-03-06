# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'introWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from matplotlib.backends import qt_compat
from os.path import expanduser
import os, stat, time
import sys
import shutil
sys.path.insert(0, './Run')


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

class AnimatedButton(QtGui.QPushButton):

    def UpdateIcon(self):
        icon = QtGui.QIcon()
        icon.addPixmap(self.iconMovie.currentPixmap())
        self.setIcon(icon)

    def __init__(self, movie, parent=None):
        super(AnimatedButton, self).__init__(parent)

        self.iconMovie = movie
        self.iconMovie.start()

        self.iconMovie.frameChanged.connect(self.UpdateIcon)

class Ui_introScreen(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
    def setupUi(self, introScreen):
        introScreen.setObjectName(_fromUtf8("introScreen"))
        introScreen.resize(392, 668)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./src/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        introScreen.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(introScreen)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.centralwidget.setAutoFillBackground(True)
        p = self.centralwidget.palette()
        p.setColor(self.centralwidget.backgroundRole(), QtCore.Qt.white)
        self.centralwidget.setPalette(p)
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        #self.wavestarButton = QtGui.QPushButton(self.centralwidget)
        self.wavestarButton = AnimatedButton(movie=QtGui.QMovie("src/Animations/WS/WS.gif"),parent=self.centralwidget)
        self.wavestarButton.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wavestarButton.sizePolicy().hasHeightForWidth())
        self.wavestarButton.setSizePolicy(sizePolicy)
        self.wavestarButton.setAutoFillBackground(False)
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("src/wavestar_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.wavestarButton.setIcon(icon)
        self.wavestarButton.setIconSize(QtCore.QSize(120, 120))
        self.wavestarButton.setDefault(False)
        self.wavestarButton.setFlat(False)
        self.wavestarButton.setObjectName(_fromUtf8("wavestarButton"))
        self.verticalLayout.addWidget(self.wavestarButton)
        #self.oysterButton = QtGui.QPushButton(self.centralwidget)
        self.oysterButton = AnimatedButton(movie=QtGui.QMovie("src/Animations/OY/OY.gif"),parent=self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oysterButton.sizePolicy().hasHeightForWidth())
        self.oysterButton.setSizePolicy(sizePolicy)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("src/oyster_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.oysterButton.setIcon(icon1)
        self.oysterButton.setIconSize(QtCore.QSize(120, 120))
        self.oysterButton.setObjectName(_fromUtf8("oysterButton"))
        self.verticalLayout.addWidget(self.oysterButton)
        #self.pelamisButton = QtGui.QPushButton(self.centralwidget)
        self.pelamisButton = AnimatedButton(movie=QtGui.QMovie("src/Animations/PE/PE.gif"),parent=self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pelamisButton.sizePolicy().hasHeightForWidth())
        self.pelamisButton.setSizePolicy(sizePolicy)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("src/pelamis_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pelamisButton.setIcon(icon2)
        self.pelamisButton.setIconSize(QtCore.QSize(120, 120))
        self.pelamisButton.setObjectName(_fromUtf8("pelamisButton"))
        self.verticalLayout.addWidget(self.pelamisButton)
        #self.customButton = QtGui.QPushButton(self.centralwidget)
        self.customButton = AnimatedButton(movie=QtGui.QMovie("src/Animations/CU/CU.gif"),parent=self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.customButton.sizePolicy().hasHeightForWidth())
        self.customButton.setSizePolicy(sizePolicy)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("src/custom_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.customButton.setIcon(icon3)
        self.customButton.setIconSize(QtCore.QSize(120, 120))
        self.customButton.setObjectName(_fromUtf8("customButton"))
        self.verticalLayout.addWidget(self.customButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        introScreen.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(introScreen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 392, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        introScreen.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(introScreen)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        introScreen.setStatusBar(self.statusbar)

        self.retranslateUi(introScreen)
        QtCore.QMetaObject.connectSlotsByName(introScreen)

    def retranslateUi(self, introScreen):
        introScreen.setWindowTitle(_translate("introScreen", "openWEC", None))
        self.label.setText(_translate("introScreen", "Select Simulator", None))
        self.wavestarButton.setText(_translate("introScreen", "Point-Absorber Simulator", None))
        self.wavestarButton.clicked.connect(self.openWS)
        self.oysterButton.setText(_translate("introScreen", "OWSC Simulator", None))
        self.oysterButton.clicked.connect(self.openOY)
        self.pelamisButton.setText(_translate("introScreen", "Attenuator Simulator", None))
        self.pelamisButton.clicked.connect(self.openPE)
        self.customButton.setText(_translate("introScreen", "Custom Simulator", None))
        self.customButton.clicked.connect(self.openCU)
        
    def makeProjectDir(self):
        # Empty project directory
        home = expanduser("~")
        dirname = os.path.join(home,'openWEC')
        calcname = os.path.join(dirname,'Calculation')
        meshname = os.path.join(calcname,'mesh')
        resname = os.path.join(calcname,'results')
        nemohname = os.path.join(dirname,'Nemoh')
        mooringname = os.path.join(dirname,'Mooring')
        outputname = os.path.join(dirname,'Output')
        othername = os.path.join(dirname,'Other')
        if(os.path.isdir(dirname)):
            if(os.path.isdir(calcname)):
                if(os.path.isdir(meshname)):
                    None
                else:
                    os.mkdir(meshname)
                if(os.path.isdir(resname)):
                    None
                else:
                    os.mkdir(resname)
            else:
                os.mkdir(calcname)
            if(os.path.isdir(nemohname)):
                None
            else:
                os.mkdir(nemohname)
            if(os.path.isdir(mooringname)):
                None
            else:
                os.mkdir(mooringname)
            if(os.path.isdir(outputname)):
                None
            else:
                os.mkdir(outputname)
            if(os.path.isdir(othername)):
                None
            else:
                os.mkdir(othername)
#                try:
#                    shutil.rmtree(dirname)
#                except:
#                    time.sleep(0.1)
#                    shutil.rmtree(dirname)
#            time.sleep(0.1)
        else:
            os.mkdir(dirname)
            os.mkdir(calcname)
            os.mkdir(nemohname)
            os.mkdir(meshname)
            os.mkdir(resname)
            os.mkdir(mooringname)
            os.mkdir(outputname)
            os.mkdir(othername)
        # Copy necessary files
        shutil.copy('./Calculation/Solver.exe',calcname)
        shutil.copy('./Calculation/input.txt',calcname)
        shutil.copy('./Calculation/preProcessor.exe',calcname)
        shutil.copy('./Calculation/Mesh.cal',calcname)
        shutil.copy('./Calculation/Nemoh.cal',calcname)
        shutil.copy('./Calculation/postProc',calcname)
        shutil.copy('./Calculation/postProcO',calcname)
        shutil.copy('./Calculation/meshL',calcname)
        shutil.copy('./Calculation/meshO',calcname)
        shutil.copy('./Calculation/solver',calcname)
        shutil.copy('./Calculation/solverO',calcname)
        shutil.copy('./Calculation/postProcessor.exe',calcname)
        shutil.copy('./Calculation/ID.dat',calcname)
        shutil.copy('./Calculation/Mesh.exe',calcname)
        shutil.copy('./Calculation/preProc',calcname)
        shutil.copy('./Calculation/preProcO',calcname)
        shutil.copy('./Run/spec_test.dat',othername)
        shutil.copy('./Mooring/lines_template.txt',mooringname)
        shutil.copy('./Mooring/lines.txt',mooringname)
        # Give permissions to executables
        os.chmod(os.path.join(calcname,'meshL'),stat.S_IRWXU)
        os.chmod(os.path.join(calcname,'preProc'),stat.S_IRWXU)
        os.chmod(os.path.join(calcname,'solver'),stat.S_IRWXU)
        os.chmod(os.path.join(calcname,'postProc'),stat.S_IRWXU)
        os.chmod(os.path.join(calcname,'meshO'),stat.S_IRWXU)
        os.chmod(os.path.join(calcname,'preProcO'),stat.S_IRWXU)
        os.chmod(os.path.join(calcname,'solverO'),stat.S_IRWXU)
        os.chmod(os.path.join(calcname,'postProcO'),stat.S_IRWXU)
        
      
    def openWS(self):
        import openWEC_WS as opc
        self.makeProjectDir()
        oldwindow = self
        window = opc.openWS()
        self = window
        window.show()
        oldwindow.close()
        
    def openOY(self):
        import openWEC_OY as opc
        self.makeProjectDir()
        oldwindow = self
        window = opc.openOY()
        self = window
        window.show()
        oldwindow.close()
        
    def openPE(self):
        import openWEC_PE as opc
        self.makeProjectDir()
        oldwindow = self
        window = opc.openPE()
        self = window
        window.show()
        oldwindow.close()

    def openCU(self):
        import openWEC_custom as opc
        self.makeProjectDir()
        oldwindow = self
        window = opc.openCustom()
        self = window
        window.show()
        oldwindow.close()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_introScreen()
    ex.show()
    sys.exit(app.exec_())
